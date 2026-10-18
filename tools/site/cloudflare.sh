#!/usr/bin/env bash
# Deploy _site/ to Cloudflare Pages and serve it at bible.apphaus.us (run by .github/workflows/pages.yml).
# Needs CLOUDFLARE_API_TOKEN (Account › Cloudflare Pages › Edit; Zone › DNS › Edit and Zone › Zone › Read on apphaus.us)
# and CLOUDFLARE_ACCOUNT_ID. Every step is idempotent: the first run creates the Pages project, attaches the custom
# domain and adds the DNS record; later runs only deploy.
set -euo pipefail
PROJECT="${CF_PROJECT:-bible}"
DOMAIN="${CF_DOMAIN:-bible.apphaus.us}"
ZONE="${DOMAIN#*.}"
API=https://api.cloudflare.com/client/v4
ACC="$API/accounts/$CLOUDFLARE_ACCOUNT_ID"
cf() { curl -sS -H "Authorization: Bearer $CLOUDFLARE_API_TOKEN" -H "Content-Type: application/json" "$@"; }

# 1. the Pages project (direct upload, production branch master)
if [ "$(cf "$ACC/pages/projects/$PROJECT" | jq -r .success)" != "true" ]; then
  echo "creating Pages project $PROJECT"
  cf -X POST "$ACC/pages/projects" -d "{\"name\":\"$PROJECT\",\"production_branch\":\"master\"}" | jq -e .success >/dev/null
fi
SUB="$(cf "$ACC/pages/projects/$PROJECT" | jq -r .result.subdomain)"   # e.g. bible.pages.dev (or bible-xyz.pages.dev)

# 2. upload the site
npx --yes wrangler@3 pages deploy _site --project-name="$PROJECT" --branch=master --commit-dirty=true

# 3. the custom domain on the project
if ! cf "$ACC/pages/projects/$PROJECT/domains" | jq -e --arg d "$DOMAIN" '.result[] | select(.name == $d)' >/dev/null; then
  echo "attaching $DOMAIN to $PROJECT"
  cf -X POST "$ACC/pages/projects/$PROJECT/domains" -d "{\"name\":\"$DOMAIN\"}" | jq -c '{success, errors}'
fi

# 4. DNS: a proxied CNAME DOMAIN -> the project's pages.dev name
ZID="$(cf "$API/zones?name=$ZONE" | jq -r '.result[0].id')"
REC="$(cf "$API/zones/$ZID/dns_records?name=$DOMAIN" | jq -c '.result[0] // empty')"
BODY="{\"type\":\"CNAME\",\"name\":\"$DOMAIN\",\"content\":\"$SUB\",\"proxied\":true,\"comment\":\"Bible Manga (Cloudflare Pages)\"}"
if [ -z "$REC" ]; then
  echo "adding CNAME $DOMAIN -> $SUB"
  cf -X POST "$API/zones/$ZID/dns_records" -d "$BODY" | jq -c '{success, errors}'
elif [ "$(jq -r .content <<<"$REC")" != "$SUB" ]; then
  echo "pointing $DOMAIN at $SUB (was $(jq -r .content <<<"$REC"))"
  cf -X PUT "$API/zones/$ZID/dns_records/$(jq -r .id <<<"$REC")" -d "$BODY" | jq -c '{success, errors}'
fi
echo "https://$DOMAIN  (also https://$SUB)"

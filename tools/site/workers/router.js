// The Worker "bible", which owns bible.apphaus.us: it serves no pages itself. /<lang>/… goes to that language's Worker
// (bible-es …, each with its own static assets and file limit), everything else to bible-en (English, the domain root).
export default {
  async fetch(request, env) {
    const url = new URL(request.url);
    const m = url.pathname.match(/^\/([a-z]{2})(\/|$)/);
    const site = m && m[1] !== "en" ? env[m[1].toUpperCase()] : null;
    if (site) {
      if (!m[2]) return Response.redirect(`${url.origin}/${m[1]}/${url.search}`, 301);
      return site.fetch(request);
    }
    return env.EN.fetch(request);
  },
};

"""Injects the 'more than a website' section into a demo page (idempotent)."""
import sys, re, html
T = {
 'af': dict(h="Begin met die webwerf. Groei wanneer jy gereed is.",
   p="Hierdie demo stuur navrae na WhatsApp. Later kan daar 'n hele stelsel agter jou webwerf wees, net as dit vir jou sin maak.",
   c=[("Die webwerf","Jou eie webwerf en e-posadresse, soos hierdie demo. Navrae kom op WhatsApp en e-pos."),
      ("Die webwerf en jou eie stelsel","Elke navraag, bespreking en kliënt op een plek, met herinneringe en opvolge wat vanself gaan."),
      ("Die stelsel en Zara","Zara antwoord jou oproepe, WhatsApps, Facebook-boodskappe en die webwerf-klets, ook Sondagaand om nege-uur, en sit alles in jou stelsel.")],
   f="Ons begin waar dit vir jou sin maak, en gesels graag oor wat by jou besigheid pas.", b="Gesels met Hello Zara", now="Begin hier", later="Later, as jy wil", m="Hallo, ek het die demo-webwerf vir {name} gesien."),
 'en': dict(h="Start with the website. Grow when you're ready.",
   p="This demo sends enquiries to WhatsApp. Later there can be a whole system behind your website, only if it makes sense for you.",
   c=[("The website","Your own website and email addresses, like this demo. Enquiries arrive on WhatsApp and email."),
      ("The website and your own system","Every enquiry, booking and client in one place, with reminders and follow-ups that happen by themselves."),
      ("The system and Zara","Zara answers your calls, WhatsApps, Facebook messages and the website chat, even at nine on a Sunday night, and puts it all in your system.")],
   f="We start where it makes sense for you, and we'd love to talk about what fits your business.", b="Talk to Hello Zara", now="Start here", later="Later, if you want", m="Hi, I saw the demo website for {name}."),
}
CSS = """<style id="hz-more-css">
.hz-more{padding:80px 0;background:#f7f5f9;color:#25212b;font-family:inherit}
.hz-more .hz-w{max-width:1180px;margin:0 auto;padding:0 24px}
.hz-more .hz-tag{font:700 12px/1 system-ui,sans-serif;letter-spacing:.14em;color:#7a3e9d;text-transform:uppercase;margin-bottom:10px}
.hz-more h2{font-size:clamp(30px,3.6vw,46px);margin:0 0 12px;line-height:1.1}
.hz-more .hz-p{max-width:60ch;margin:0 0 30px;color:#5a5262}
.hz-more ol{list-style:none;margin:0;padding:0;display:grid;grid-template-columns:1.4fr 1fr 1fr;gap:16px;counter-reset:hz;align-items:stretch}
.hz-more li{counter-increment:hz;background:#fff;border:1px solid #e5dcea;border-radius:14px;padding:22px}
.hz-more li::before{content:counter(hz);display:inline-grid;place-items:center;width:30px;height:30px;border-radius:50%;background:#7a3e9d;color:#fff;font:700 15px system-ui,sans-serif;margin-bottom:12px}
.hz-more li em{display:block;font:700 11px system-ui,sans-serif;letter-spacing:.12em;text-transform:uppercase;color:#7a3e9d;font-style:normal;margin-bottom:6px}
.hz-more li.hz-now{border:2px solid #7a3e9d;box-shadow:0 18px 40px rgba(122,62,157,.14);padding:26px}
.hz-more li.hz-now b{font-size:23px}
.hz-more li.hz-later{background:transparent;border-style:dashed;opacity:.85}
.hz-more li.hz-later::before{background:#cdb9da}
.hz-more li.hz-later em{color:#8a7f92}
.hz-more li b{display:block;font-size:19px;margin-bottom:6px}
.hz-more li span{color:#5a5262;font-size:15px;line-height:1.5}
.hz-more .hz-f{display:flex;flex-wrap:wrap;align-items:center;gap:16px;margin-top:26px}
.hz-more .hz-f p{margin:0;color:#5a5262}
.hz-more .hz-b{display:inline-block;background:#7a3e9d;color:#fff;text-decoration:none;font:700 15px system-ui,sans-serif;padding:13px 22px;border-radius:999px}
.hz-more .hz-b:hover{background:#5f2f7b}
.hz-more .hz-by{font-size:13px;color:#857c8c;margin-top:14px}
@media (max-width:820px){.hz-more ol{grid-template-columns:1fr}.hz-more{padding:60px 0}.hz-more .hz-w{padding:0 16px}}
</style>"""
def block(lang, name):
    t = T[lang]; e = html.escape
    from urllib.parse import quote
    tags = (t['now'], t['later'], t['later'])
    lis = ''.join(f'<li class="{"hz-now" if i == 0 else "hz-later"}"><em>{e(tags[i])}</em><b>{e(a)}</b><span>{e(b)}</span></li>' for i, (a, b) in enumerate(t['c']))
    wa = 'https://wa.me/27788617650?text=' + quote(t['m'].format(name=name))
    return f'''<section class="hz-more" id="meer" aria-label="{e(t["h"])}"><div class="hz-w">
<div class="hz-tag">Hello Zara</div><h2>{e(t["h"])}</h2><p class="hz-p">{e(t["p"])}</p>
<ol>{lis}</ol>
<div class="hz-f"><p>{e(t["f"])}</p><a class="hz-b" href="{wa}" target="_blank" rel="noopener">{e(t["b"])}</a></div>
</div></section>'''
def inject(path, lang, name, before):
    s = open(path, encoding='utf-8').read()
    s = re.sub(r'<style id="hz-more-css">.*?</style>', '', s, flags=re.S)
    s = re.sub(r'<section class="hz-more".*?</section>', '', s, flags=re.S)
    s = s.replace('</head>', CSS + '</head>', 1)
    i = s.find(before)
    assert i > 0, (path, before)
    s = s[:i] + block(lang, name) + '\n' + s[i:]
    open(path, 'w', encoding='utf-8').write(s)
if __name__ == '__main__':
    inject(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])

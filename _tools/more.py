"""Injects the 'more than a website' section into a demo page (idempotent)."""
import sys, re, html
T = {
 'af': dict(h="Meer as 'n webwerf, as jy wil",
   p="Hierdie demo stuur navrae na WhatsApp. Agter jou webwerf kan ook 'n hele stelsel wees, as dit vir jou sin maak. Jy kies wat jy nodig het.",
   c=[("Die webwerf","Jou eie webwerf en e-posadresse, soos hierdie demo. Navrae kom op WhatsApp en e-pos."),
      ("Die webwerf en jou eie stelsel","Elke navraag, bespreking en kliënt op een plek, met herinneringe en opvolge wat vanself gaan."),
      ("Die stelsel en Zara","Zara antwoord jou oproepe, WhatsApps, Facebook-boodskappe en die webwerf-klets, ook Sondagaand om nege-uur, en sit alles in jou stelsel.")],
   f="Die koste hang af van wat jy kies. Ons gesels graag oor wat by jou besigheid pas.", b="Gesels met Hello Zara", m="Hallo, ek het die demo-webwerf vir {name} gesien."),
 'en': dict(h="More than a website, if you want it",
   p="This demo sends enquiries to WhatsApp. Behind your website there can also be a whole system, if it makes sense for you. You choose what you need.",
   c=[("The website","Your own website and email addresses, like this demo. Enquiries arrive on WhatsApp and email."),
      ("The website and your own system","Every enquiry, booking and client in one place, with reminders and follow-ups that happen by themselves."),
      ("The system and Zara","Zara answers your calls, WhatsApps, Facebook messages and the website chat, even at nine on a Sunday night, and puts it all in your system.")],
   f="The cost depends on what you choose. We'd love to talk about what fits your business.", b="Talk to Hello Zara", m="Hi, I saw the demo website for {name}."),
}
CSS = """<style id="hz-more-css">
.hz-more{padding:80px 0;background:#f7f5f9;color:#25212b;font-family:inherit}
.hz-more .hz-w{max-width:1180px;margin:0 auto;padding:0 24px}
.hz-more .hz-tag{font:700 12px/1 system-ui,sans-serif;letter-spacing:.14em;color:#7a3e9d;text-transform:uppercase;margin-bottom:10px}
.hz-more h2{font-size:clamp(30px,3.6vw,46px);margin:0 0 12px;line-height:1.1}
.hz-more .hz-p{max-width:60ch;margin:0 0 30px;color:#5a5262}
.hz-more ol{list-style:none;margin:0;padding:0;display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:16px;counter-reset:hz}
.hz-more li{counter-increment:hz;background:#fff;border:1px solid #e5dcea;border-radius:14px;padding:22px}
.hz-more li::before{content:counter(hz);display:inline-grid;place-items:center;width:30px;height:30px;border-radius:50%;background:#7a3e9d;color:#fff;font:700 15px system-ui,sans-serif;margin-bottom:12px}
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
    lis = ''.join(f'<li><b>{e(a)}</b><span>{e(b)}</span></li>' for a, b in t['c'])
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

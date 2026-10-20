import json, html, os
D = '/home/claude/hellozara-demos/'
e = html.escape

AF = dict(lang='af', demo_note='\'n Demo-webwerf wat Hello Zara vir {owner} by {name} ontwerp het. Niks hier is lewendig voor {they} ja sê nie.',
          nav=['Geleenthede', 'Foto\'s', 'Datum', 'Kontak'], cta='Is my datum oop?', events_eyebrow='wat ons aanbied',
          gallery_eyebrow='by {name}', form_eyebrow='kyk of jou datum oop is', form_title='Vra vir jou datum',
          form_sub='Dit neem minder as \'n minuut. Dit word \'n WhatsApp-boodskap aan {owner}.',
          kind='Wat beplan jy?', date='Datum', guests='Aantal gaste', yourname='Jou naam', extra='Enigiets anders?',
          extra_ph='Die tyd, die tema, vrae…', out='JOU BOODSKAP AAN {OWNER}', send='Stuur op WhatsApp',
          small='Demo: in die lewendige weergawe land dit ook in {owner} se inboks, en jy kry \'n bevestiging.',
          contact_eyebrow='kom kuier', contact_title='Kontak {owner}', call='Bel of WhatsApp', email='E-pos', where='Waar',
          maps='Wys op Google Maps', wa_btn='WhatsApp {owner}', footer='Demo deur', review_src='Google-resensie',
          zara_btn='Vra vir Zara', zara_sub='{owner} se assistent (demo)', zara_hi='Hallo! Ek is Zara, {owner} se assistent by {name}. Ek kan kyk of jou datum oop is of \'n vinnige vraag beantwoord.',
          q_date='Is my datum oop?', q_what='Wat bied julle aan?', q_where='Waar is julle?', q_price='Hoeveel kos dit?',
          ask_ph='Tik jou vraag…', send_short='Stuur', chat_note='Demo-klets deur Hello Zara',
          f1='Lekker! Watter soort geleentheid is dit?', f2='Op watter datum?', f3='Ongeveer hoeveel gaste?', f4='Laaste een: wat is jou naam?',
          f5='Dankie, {n}! Ek het genoteer: {k}, {d}, ongeveer {g} gaste.', f6='In die lewendige weergawe kry {owner} dit dadelik en laat sy weet of die datum oop is. Jy kry ook \'n herinnering.',
          unk='Goeie vraag! Ek sal sorg dat {owner} dit sien. Jy kan ook WhatsApp na {phone}.',
          msg_hi='Hallo{greet}{n}! Ek beplan \'n {k} en wil graag weet of my datum nog oop is.', msg_date='Datum', msg_g='Aantal gaste', msg_x='Verder', dis=', dis ',
          rx_date='datum|oop|beskikbaar|boek|bespreek', rx_price='prys|hoeveel|koste|r\\d', rx_where='waar|adres|ligging|ry', rx_what='wat|bied|doen|troue|funksie|partytjie')
EN = dict(lang='en', demo_note='A demo website Hello Zara designed for {owner} at {name}. Nothing here is live until {they} say yes.',
          nav=['Events', 'Photos', 'Dates', 'Contact'], cta='Is my date open?', events_eyebrow='what we host',
          gallery_eyebrow='at {name}', form_eyebrow='check your date', form_title='Ask about your date',
          form_sub='It takes less than a minute and becomes a WhatsApp message to {owner}.',
          kind='What are you planning?', date='Date', guests='Number of guests', yourname='Your name', extra='Anything else?',
          extra_ph='The time, the theme, questions…', out='YOUR MESSAGE TO {OWNER}', send='Send on WhatsApp',
          small='Demo: in the live version this also lands in {owner}\'s inbox and you get a confirmation.',
          contact_eyebrow='come and visit', contact_title='Contact {owner}', call='Call or WhatsApp', email='Email', where='Where',
          maps='Show on Google Maps', wa_btn='WhatsApp {owner}', footer='Demo by', review_src='Google review',
          zara_btn='Ask Zara', zara_sub='{owner}\'s assistant (demo)', zara_hi='Hi! I\'m Zara, {owner}\'s assistant at {name}. I can check whether your date is open or answer a quick question.',
          q_date='Is my date open?', q_what='What do you host?', q_where='Where are you?', q_price='What does it cost?',
          ask_ph='Type your question…', send_short='Send', chat_note='Demo chat by Hello Zara',
          f1='Lovely! What kind of event is it?', f2='Which date?', f3='Roughly how many guests?', f4='Last one: what\'s your name?',
          f5='Thank you, {n}! I\'ve noted: {k}, {d}, about {g} guests.', f6='In the live version {owner} gets this straight away and lets you know if the date is open. You also get a reminder.',
          unk='Good question! I\'ll make sure {owner} sees it. You can also WhatsApp {phone}.',
          msg_hi='Hi{greet}{n}! I\'m planning a {k} and would love to know if my date is still open.', msg_date='Date', msg_g='Guests', msg_x='Also', dis=', it\'s ',
          rx_date='date|open|availab|book', rx_price='price|cost|how much|r\\d', rx_where='where|address|location|directions', rx_what='what|host|offer|wedding|party|function')

VENUES = [
 dict(slug='plaasdam', L=AF, name='Die Plaasdam', owner='Nita', they='sy', title='Die Plaasdam · Troue- en funksielokaal · Vereeniging',
      desc='Troues en funksies op \'n plaas in Sonland Park, Vereeniging: tuine, koi-damme en volstruise wat rondloop.',
      fonts='family=Pinyon+Script&family=Cormorant+Garamond:ital,wght@0,500;0,600;1,500&family=Nunito+Sans:wght@400;600;700',
      head='"Cormorant Garamond",Georgia,serif', body='"Nunito Sans",system-ui,sans-serif', script='"Pinyon Script",cursive',
      c=dict(a='#4f7f73', a2='#36594f', bg='#f7f4ee', panel='#e7efe9', ink='#2e3a35', muted='#5f6f68', line='#d8e2db', dark='#24332d', accent='#f1d9c6', soft='#efe1e1'),
      logo='img/logo.jpg', brand_line='TROUE- EN FUNKSIELOKAAL',
      hero='img/windmill.jpg', hero_alt='Die windpomp en \'n ligblou kombi in die veld by Die Plaasdam met sonsondergang',
      h1='Jou troue op <em>die plaas</em>.', lead='Rustieke bosveld, mooi versorgde tuine en koi-damme, met volstruise en springbokke wat rondloop. In Sonland Park, Vereeniging.',
      proof=[('4,8', 'op Google (82 resensies)'), ('10K', 'volgers op Facebook')],
      events_title='Van die seremonie tot die laaste dans.', events_intro='Sê vir Nita watter dag jy in gedagte het. Sy laat weet of dit oop is.',
      events=[('Troues', 'Die seremonie, die onthaal en die foto\'s in die veld by die windpomp.'), ('Funksies', 'Verjaarsdae, jaareindfunksies en ander groot dae.'), ('Lekker boerekos', 'Gaste skryf self oor die kos: "baie lekker kos by die trou venue".')],
      kinds=['Troue', 'Verjaarsdag', 'Jaareindfunksie', 'Ander funksie'],
      gallery=[('img/hall.jpg', 'Die onthaal-saal met liggies en die dansvloer'), ('img/table.jpg', 'Lang houttafels met groen lopers'), ('img/windmill.jpg', 'Die windpomp in die veld')],
      side='img/sweetheart.jpg', side_alt='Die bruidspaar se tafel met blomme, liggies en \'n sluier teen die baksteenmuur',
      quote='Best around the Vaal Triangle', quote_by='Ronel',
      phone='082 325 2268', wa='27823252268', mail='maineverster@gmail.com', addr='84 Helena van Zyl St, Sonland Park, Vereeniging',
      maps='https://www.google.com/maps/search/?api=1&query=Die+Plaasdam+Vereeniging', fb='https://www.facebook.com/Plaasdam',
      a_what='Die Plaasdam is \'n troue- en funksielokaal met tuine, koi-damme en volstruise en springbokke op die plaas. Ons hou troues, verjaarsdae en ander funksies.',
      a_where='Ons is by 84 Helena van Zyl St, Sonland Park, Vereeniging.',
      a_price='Elke dag is anders, so Nita stuur vir jou \'n kwotasie vir jou datum en aantal gaste. Sal ek vir jou datum vra?',
      motif='windmill'),
 dict(slug='winebarrel', L=EN, name='The Wine Barrel', owner='Denise', they='she', title='The Wine Barrel · Venue · Stephanopark, Vanderbijlpark',
      desc='The perfect venue for any function or celebration in Stephanopark, Vanderbijlpark: weddings, baby showers, birthdays and engagements.',
      fonts='family=Cormorant+SC:wght@500;600&family=Cormorant+Garamond:ital,wght@0,500;1,500&family=Great+Vibes&family=Lato:wght@400;700',
      head='"Cormorant SC",Georgia,serif', body='"Lato",system-ui,sans-serif', script='"Great Vibes",cursive',
      c=dict(a='#b8924a', a2='#9a7733', bg='#f5f0e6', panel='#ebe3d2', ink='#2a2a22', muted='#62604f', line='#ddd2bb', dark='#1d3326', accent='#d9b56a', soft='#e9e2d0'),
      logo=None, brand_line='STEPHANOPARK · VANDERBIJLPARK',
      hero='img/hero.jpg', hero_alt='A table set with white roses, eucalyptus, candles and white chairs against a brick wall',
      h1='Your dream event <em>starts here</em>.', lead='From intimate celebrations to grand occasions, we make every moment special. Venue hire for all functions and events in Stephanopark, Vanderbijlpark.',
      proof=[('4.3', 'on Google (157 reviews)'), ('92%', 'recommend us on Facebook')],
      events_title='The perfect venue for any celebration.', events_intro='Tell Denise what you are celebrating. She will let you know if your date is open and send a quote.',
      events=[('Weddings', 'Say "I do" under the willow trees.'), ('Baby showers', 'Small moments that make big memories.'), ('Birthdays', 'Celebrate with good food and great company.'), ('Engagements', 'The start of the next chapter.'), ('Private functions & more', 'Venue, decoration, catering and personalised service.')],
      kinds=['Wedding', 'Baby shower', 'Birthday', 'Engagement', 'Private function'],
      gallery=[('img/barrel.jpg', 'A wine barrel with succulents and a candle'), ('img/hero.jpg', 'White roses, eucalyptus and candlelight against the brick wall')],
      side='img/headtable.jpg', side_alt='The head table with a wooden backdrop, fairy lights and greenery',
      quote='Beautiful venue and exquisite food. You will not regret a moment.', quote_by='Thea',
      phone='079 711 7059', wa='27797117059', mail='vlei119@icloud.com', addr='119 Vlei Street, Stephanopark, Vanderbijlpark',
      maps='https://www.google.com/maps/search/?api=1&query=The+Wine+Barrel+Stephanopark+Vanderbijlpark', fb='https://www.facebook.com/profile.php?id=100063832741679',
      a_what='We host weddings, baby showers, birthdays, engagements and private functions. We offer the venue, decoration, delicious food and catering.',
      a_where='We are at 119 Vlei Street, Stephanopark, Vanderbijlpark.',
      a_price='Every event is different, so Denise sends a quote for your date and number of guests. Shall I ask about your date?',
      motif='gold'),
 dict(slug='mountridge', L=EN, name='Mountridge Events', owner='Leonie', they='she', title='Mountridge Events · Function Venue · Houtkop, Vereeniging',
      desc='A charming thatched function venue in Houtkop, Vereeniging for up to 100 guests: intimate weddings, family gatherings and corporate retreats.',
      fonts='family=Mrs+Saint+Delafield&family=Cormorant+Garamond:ital,wght@0,500;0,600;1,500&family=Karla:wght@400;600;700',
      head='"Cormorant Garamond",Georgia,serif', body='"Karla",system-ui,sans-serif', script='"Mrs Saint Delafield",cursive',
      c=dict(a='#3f4f3e', a2='#2e3b2d', bg='#f6f2ea', panel='#ece4d4', ink='#2b2a26', muted='#655f53', line='#ddd3c0', dark='#2b2a26', accent='#b08850', soft='#efe6d6'),
      logo='img/logo.jpg', brand_line='FUNCTION VENUE · EST 2016',
      hero='img/chairs.jpg', hero_alt='Rows of white-covered chairs under the high thatched roof at Mountridge',
      h1='Where special occasions become <em>lasting memories</em>.', lead='A charming thatched venue for up to 100 guests: intimate weddings, family gatherings, corporate retreats and more. In Houtkop, Vereeniging.',
      proof=[('4.4', 'on Google (44 reviews)'), ('100', 'guests at most')],
      events_title='Made for the days that matter.', events_intro='Tell Leonie about your day. She will let you know if the date is open.',
      events=[('Intimate weddings', 'Up to 100 guests under the thatch.'), ('Family gatherings', 'Birthdays and celebrations with the people you love.'), ('Corporate retreats', 'Team days and functions away from the office.'), ('And more', 'Bridal showers, year-end functions and special days.')],
      kinds=['Wedding', 'Family celebration', 'Corporate', 'Other'],
      gallery=[('img/t2.jpg', 'Tables set in the hall'), ('img/t1.jpg', 'Blue napkins and wildflowers'), ('img/t3.jpg', 'Lilac and wildflowers'), ('img/t4.jpg', 'White chairs and soft light'), ('img/tea.jpg', 'The tea and coffee station')],
      side='img/tea.jpg', side_alt='A tea and coffee station with juice dispensers in the thatched hall',
      quote='Mountridge is an absolute gem of a venue and Leonie goes the extra mile to ensure your event is special.', quote_by='Carrol-Lynne',
      phone='074 444 9627', wa='27744449627', mail='info@mountridgevenue.co.za', addr='34 Langrand Rd, Houtkop AH, Vereeniging',
      maps='https://www.google.com/maps/search/?api=1&query=Mountridge+Events+Function+Venue+Vereeniging', fb='https://www.facebook.com/MountridgeEventsFunctionVenue',
      a_what='Mountridge is a thatched function venue for up to 100 guests: intimate weddings, family gatherings, corporate retreats and more.',
      a_where='We are at 34 Langrand Rd, Houtkop AH, Vereeniging.',
      a_price='Every event is different, so Leonie sends a quote for your date and number of guests. Shall I ask about your date?',
      motif='thatch', split=True),
 dict(slug='nelvida', L=EN, name='The Nelvida Venue', owner='Danielle', they='she', title='The Nelvida Venue · Unitaspark, Vereeniging',
      desc='Your perfect venue for every occasion in Unitaspark, Vereeniging: birthdays, baby showers, weddings, corporate events and year-end functions.',
      fonts='family=Cinzel:wght@500;600&family=Great+Vibes&family=Poppins:wght@400;500;600',
      head='"Cinzel",Georgia,serif', body='"Poppins",system-ui,sans-serif', script='"Great Vibes",cursive',
      c=dict(a='#c8306b', a2='#a32254', bg='#fffaf4', panel='#fdeee6', ink='#1f1d1d', muted='#5f5656', line='#f0ddd2', dark='#1f1d1d', accent='#c8a24a', soft='#fdf3dc'),
      logo='img/logo.jpg', brand_line='VENUE · ESTD 2022',
      hero='img/flowers.jpg', hero_alt='Bright gerberas, roses and statice in coloured glass bottles on a dressed table at Nelvida',
      h1='The venue where <em>memories are made</em>.', lead='Your perfect venue for every occasion: a spacious venue, lush gardens and outdoor areas, and a fully equipped kitchen and bar. In Unitaspark, Vereeniging.',
      proof=[('4.7', 'on Google (15 reviews)'), ('2027', 'bookings now open')],
      events_title='Your perfect venue for every occasion.', events_intro='Flexible packages to suit your needs. Ask Danielle about your date.',
      events=[('Birthdays', 'Celebrate life\'s special moments.'), ('Baby showers', 'Small moments create big memories.'), ('Weddings', 'Say "I do" in a beautiful setting.'), ('Corporate events', 'Professional spaces for successful events.'), ('Year-end functions', 'Reward your team in style.')],
      kinds=['Birthday', 'Baby shower', 'Wedding', 'Corporate event', 'Year-end function'],
      avail=[('November', '7 and 28 November'), ('December', '11 and 13 December, for year-end functions during the week')], avail_note='From Danielle\'s latest availability post. Fridays and Sundays on request.',
      gallery=[('img/lanterns.jpg', 'Paper lanterns and bright flowers'), ('img/flowers.jpg', 'Gerberas and roses in coloured bottles')],
      side='img/lanterns.jpg', side_alt='Tables with paper lanterns, white chairs and bright flowers at Nelvida',
      quote='A beautiful venue in a very peaceful setting', quote_by='Matsie',
      phone='084 662 4100', wa='27846624100', mail='vandeventerdanielle131@gmail.com', addr='17 Herby Taylor Street, Unitaspark, Vereeniging',
      maps='https://www.google.com/maps/search/?api=1&query=Nelvida+Unitaspark+Vereeniging', fb='https://www.facebook.com/profile.php?id=100083120026863',
      a_what='We host birthdays, baby showers, weddings, corporate events and year-end functions. There are lush gardens, outdoor areas and a fully equipped kitchen and bar.',
      a_where='We are at 17 Herby Taylor Street, Unitaspark, Vereeniging.',
      a_price='We have flexible packages to suit your needs. Danielle sends a quote for your date. Shall I ask about your date?',
      motif='flowers', split=True),
 dict(slug='oneotwo', L=AF, name='Venue OneOtwo', owner='die eienaars', greet='', they='julle', ct='Kontak ons', wab='WhatsApp ons', zsub='Venue OneOtwo se assistent (demo)', title='Venue OneOtwo · Selfsorg-lokaal · Vaalview, Vanderbijlpark',
      desc='\'n Skoon en ruim selfsorg-lokaal vir enige funksie of troue in Vaalview, Vanderbijlpark. Tafels, stoele, breekgoed en tafeldoeke ingesluit.',
      fonts='family=Kaushan+Script&family=Josefin+Sans:wght@400;600;700',
      head='"Josefin Sans",system-ui,sans-serif', body='"Josefin Sans",system-ui,sans-serif', script='"Kaushan Script",cursive',
      c=dict(a='#0f8f93', a2='#0b6d70', bg='#f5f8f8', panel='#e3f0f0', ink='#20282b', muted='#56656a', line='#d3e3e3', dark='#1d2427', accent='#19c3c3', soft='#e9f5f5'),
      logo='img/logo.jpg', brand_line='SELFSORG-LOKAAL · VAALVIEW',
      hero='img/cover.jpg', hero_alt='\'n Tafel met wit rose, groen takkies en liggies by Venue OneOtwo',
      h1='Jou eie idees, <em>ons lokaal</em>.', lead='\'n Skoon en ruim selfsorg-lokaal vir enige funksie of troue. Tafels, stoele, breekgoed, eetgerei, glase en tafeldoeke is ingesluit teen \'n bekostigbare prys.',
      proof=[('5,0', 'op Google (8 resensies)'), ('Selfsorg', 'met eie drank en eetgoed')],
      events_title='Maak dit joune.', events_intro='Bring jou eie tafeldekor, drank en eetgoed. As jy nie lus is vir kosmaak nie, kan ons spysenier help.',
      events=[('Troues', 'Gaste skryf: "Lovely wedding venue."'), ('Verlowings', '"I rented it for my engagement party."'), ('Funksies', 'Konfirmasies, verjaarsdae en ander geleenthede.'), ('Spysenier', 'Beskikbaar as jy verkies.')],
      kinds=['Troue', 'Verlowing', 'Verjaarsdag', 'Ander funksie'],
      gallery=[('img/hall.jpg', 'Die saal met wit gordyne, lanterns en liggies'), ('img/buffet.jpg', '\'n Buffettafel teen die wit gordyne')],
      side='img/hall.jpg', side_alt='Die saal met wit gordyne, liggies, lanterns en stoele met strikke',
      quote='Beautiful Venue. Venue itself decorated beautiful.', quote_by='Sharon',
      phone='073 188 3055', wa='27731883055', mail='venueoneotwo@gmail.com', addr='102 Charles Stevens St, Vaalview AH, Vanderbijlpark',
      maps='https://www.google.com/maps/search/?api=1&query=Venue+OneOtwo+Vaalview+Vanderbijlpark', fb='https://www.facebook.com/profile.php?id=100063672122055',
      a_what='Venue OneOtwo is \'n selfsorg-lokaal vir troues en funksies. Tafels, stoele, breekgoed, eetgerei, glase en tafeldoeke is ingesluit, en \'n spysenier is beskikbaar as jy verkies.',
      a_where='Ons is by 102 Charles Stevens St, Vaalview AH, Vanderbijlpark. Maak asseblief \'n afspraak om te kom kyk.',
      a_price='Die prys sluit tafels, stoele, breekgoed en tafeldoeke in. Ons stuur vir jou \'n kwotasie vir jou datum. Sal ek vir jou datum vra?',
      motif='lights'),
]

CSS = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'venue.css')).read()

def page(v):
    L = v['L']; o = v['owner']; nm = v['name']
    fmt = lambda s: s.replace('{greet}', (' '+v.get('greet', o)) if v.get('greet', o) else '').replace('{owner}', o).replace('{OWNER}', o.upper()).replace('{name}', nm).replace('{they}', v['they'])
    c = v['c']
    root = ';'.join(f'--{k}:{val}' for k, val in c.items())
    brand = (f'<img src="{v["logo"]}" alt="" width="52" height="52">' if v['logo'] else '') + \
            f'<div><span>{e(nm)}</span><small>{e(v["brand_line"])}</small></div>'
    events = ''.join(f'<li><div><h3>{e(t)}</h3><p>{e(d)}</p></div><a href="#datum" data-kind="{e(v["kinds"][min(i, len(v["kinds"])-1)])}">{"Vra →" if L is AF else "Ask →"}</a></li>' for i, (t, d) in enumerate(v['events']))
    opts = ''.join(f'<label><input type="radio" name="kind" value="{e(k)}"{" checked" if i == 0 else ""}><span>{e(k)}</span></label>' for i, k in enumerate(v['kinds']))
    gal = ''.join(f'<figure><img src="{s}" alt="{e(a)}" loading="lazy"><figcaption>{e(a)}</figcaption></figure>' for s, a in v['gallery'])
    avail = ''
    if v.get('avail'):
        avail = '<div class="avail"><b>Open dates</b><ul>' + ''.join(f'<li><strong>{e(m)}</strong> {e(d)}</li>' for m, d in v['avail']) + f'</ul><p>{e(v["avail_note"])}</p></div>'
    proof = ''.join(f'<span><b>{e(a)}</b> {e(b)}</span>' for a, b in v['proof'])
    js = dict(WA=v['wa'], L={k: fmt(val) if isinstance(val, str) else val for k, val in L.items()}, A=dict(what=v['a_what'], where=v['a_where'], price=v['a_price']), phone=v['phone'], owner=o)
    return f'''<!doctype html>
<html lang="{L["lang"]}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="robots" content="noindex,nofollow">
<title>{e(v["title"])}</title>
<meta name="description" content="{e(v["desc"])}">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?{v["fonts"]}&display=swap" rel="stylesheet">
<style>
:root{{{root};--head:{v["head"]};--body:{v["body"]};--script:{v["script"]}}}
{CSS}
</style>
</head>
<body class="m-{v["motif"]}">
<div class="demo-note">{e(fmt(L["demo_note"]))} <a href="https://hellozara.solutions">hellozara.solutions</a></div>
<header><div class="wrap nav">
  <a class="brand" href="#top" aria-label="{e(nm)}">{brand}</a>
  <ul><li><a href="#geleenthede">{L["nav"][0]}</a></li><li><a href="#fotos">{L["nav"][1]}</a></li><li><a href="#datum">{L["nav"][2]}</a></li><li><a href="#kontak">{L["nav"][3]}</a></li></ul>
  <a class="btn" href="#datum">{e(L["cta"])}</a>
</div></header>
<main id="top">
<div class="hero{' split' if v.get('split') else ''}">
  <img src="{v["hero"]}" alt="{e(v["hero_alt"])}">
  <div class="wrap">
    <div class="script-name">{e(nm)}</div>
    <h1>{v["h1"]}</h1>
    <p>{e(v["lead"])}</p>
    <div class="actions"><a class="btn light" href="#datum">{e(L["cta"])}</a><a class="btn line" href="#fotos">{L["nav"][1]}</a></div>
    <div class="proof">{proof}</div>
  </div>
</div>
<div class="band" aria-hidden="true"></div>
<section id="geleenthede"><div class="wrap">
  <div class="head"><div><div class="eyebrow">{e(fmt(L["events_eyebrow"]))}</div><h2>{e(v["events_title"])}</h2></div><p>{e(v["events_intro"])}</p></div>
  <div class="menu"><ol>{events}</ol>
  <figure><img src="{v["side"]}" alt="{e(v["side_alt"])}" loading="lazy"></figure></div>
</div></section>
<section id="fotos" class="gallery-sec"><div class="wrap">
  <div class="head"><div><div class="eyebrow">{e(fmt(L["gallery_eyebrow"]))}</div><h2>{L["nav"][1]}</h2></div></div>
  <div class="strip n{len(v["gallery"])}">{gal}</div>
</div></section>
<section id="datum"><div class="wrap quote">
  <aside><div class="eyebrow">{e(L["form_eyebrow"])}</div><h2>{e(L["form_title"])}</h2><p>{e(fmt(L["form_sub"]))}</p>{avail}</aside>
  <form class="card" id="q" novalidate>
    <fieldset><legend>{e(L["kind"])}</legend><div class="opts">{opts}</div></fieldset>
    <div class="row"><label class="field">{e(L["date"])}<input type="date" id="d"></label><label class="field">{e(L["guests"])}<input id="g" inputmode="numeric" placeholder="60"></label></div>
    <label class="field">{e(L["yourname"])}<input id="n" autocomplete="given-name"></label>
    <label class="field">{e(L["extra"])}<textarea id="x" placeholder="{e(L["extra_ph"])}"></textarea></label>
    <div class="out" aria-live="polite"><b>{e(fmt(L["out"]))}</b><span id="msg"></span></div>
    <button class="btn" type="submit">{e(L["send"])}</button>
    <p class="small">{e(fmt(L["small"]))}</p>
  </form>
</div></section>
<section class="review"><div class="wrap"><div class="stars" aria-label="5">★★★★★</div><blockquote>“{e(v["quote"])}”</blockquote><cite>{e(v["quote_by"])}, {e(L["review_src"])}</cite></div></section>
<section id="kontak"><div class="wrap contact">
  <div><div class="eyebrow">{e(L["contact_eyebrow"])}</div><h2>{e(v.get('ct') or fmt(L["contact_title"]))}</h2>
  <dl><dt>{e(L["call"])}</dt><dd><a href="https://wa.me/{v["wa"]}" target="_blank" rel="noopener">{e(v["phone"])}</a></dd>
  <dt>{e(L["email"])}</dt><dd><a href="mailto:{e(v["mail"])}">{e(v["mail"])}</a></dd>
  <dt>{e(L["where"])}</dt><dd>{e(v["addr"])}<br><a href="{v["maps"]}" target="_blank" rel="noopener">{e(L["maps"])}</a></dd>
  <dt>Facebook</dt><dd><a href="{v["fb"]}" target="_blank" rel="noopener">{e(nm)}</a></dd></dl>
  <a class="btn" href="https://wa.me/{v["wa"]}" target="_blank" rel="noopener">{e(v.get('wab') or fmt(L["wa_btn"]))}</a></div>
  <div class="pic"><img src="{v["gallery"][0][0]}" alt="{e(v["gallery"][0][1])}" loading="lazy"></div>
</div></section>
</main>
<footer><div class="wrap"><span>© {e(nm)}</span><span>{e(L["footer"])} <a href="https://hellozara.solutions">Hello Zara</a></span></div></footer>
<button class="zara-btn" id="zo" aria-expanded="false" aria-controls="chat"><i>Z</i><span>{e(L["zara_btn"])}</span></button>
<div class="chat" id="chat" role="dialog" aria-label="Zara">
  <div class="chat-top"><div><b>Zara · {e(nm)}</b><small>{e(v.get('zsub') or fmt(L["zara_sub"]))}</small></div><button id="zc" aria-label="×">×</button></div>
  <div class="log" id="log" aria-live="polite"></div>
  <div class="quick" id="quick"><button data-q="date">{e(L["q_date"])}</button><button data-q="what">{e(L["q_what"])}</button><button data-q="where">{e(L["q_where"])}</button><button data-q="price">{e(L["q_price"])}</button></div>
  <form class="ask" id="ask"><input id="ai" placeholder="{e(L["ask_ph"])}" aria-label="{e(L["ask_ph"])}"><button>{e(L["send_short"])}</button></form>
  <div class="chat-note">{e(L["chat_note"])}</div>
</div>
<script>
const C={json.dumps(js, ensure_ascii=False)};
{open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'venue.js')).read()}
</script>
</body>
</html>'''

for v in VENUES:
    open(D + v['slug'] + '/index.html', 'w').write(page(v))
    print('built', v['slug'])

import importlib.util as _u
_s = _u.spec_from_file_location('more', os.path.join(os.path.dirname(os.path.abspath(__file__)), 'more.py')); _m = _u.module_from_spec(_s); _s.loader.exec_module(_m)
for v in VENUES:
    _m.inject(D + v['slug'] + '/index.html', v['L']['lang'], v['name'], '<footer')

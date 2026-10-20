"""Fictional sample demos per niche (no real business). Run: python3 _tools/fiction.py"""
import os, sys, runpy
T = os.path.dirname(os.path.abspath(__file__))
ns = runpy.run_path(os.path.join(T, 'build.py'))  # rebuilds the real venues too (same output)
page, AF, EN = ns['page'], ns['AF'], ns['EN']
D = ns['D']
U = lambda p, w=1600: f'https://images.unsplash.com/{p}?w={w}&q=80&auto=format&fit=crop'

EN2 = dict(EN, demo_note='A sample website by Hello Zara for a made-up venue. We build yours with your own name, photos and logo.')
AF2 = dict(AF, demo_note="'n Voorbeeld-webwerf van Hello Zara vir 'n uitgedinkte besigheid. Ons bou joune met jou eie naam, foto's en logo.",
           nav=['Ons koeke', "Foto's", 'Bestel', 'Kontak'], cta='Bestel jou koek', events_eyebrow='wat ons bak',
           form_eyebrow='bestel in een minuut', form_title='Vertel ons van jou koek',
           form_sub="Dit neem minder as 'n minuut. Dit word 'n WhatsApp-boodskap aan {owner}.",
           kind='Waarvoor is dit?', date='Vir watter datum?', guests='Vir hoeveel mense?', extra='Tema, kleure, idees?',
           extra_ph='Eenhoorns, pienk en goud, 2 lae…', contact_eyebrow='kom kuier', q_date='Kan ek bestel?', q_what='Wat bak julle?',
           zara_hi="Hallo! Ek is Zara, {owner} se assistent by {name}. Ek kan jou bestelling neem of 'n vinnige vraag beantwoord.",
           f1='Lekker! Waarvoor is die koek?', f2='Vir watter datum?', f3='Vir ongeveer hoeveel mense?',
           f5='Dankie, {n}! Ek het genoteer: {k}, {d}, vir ongeveer {g} mense.',
           f6="In die lewendige weergawe kry {owner} dit dadelik en laat sy weet of die datum oop is en wat dit kos.",
           msg_hi="Hallo{greet}{n}! Ek wil graag 'n koek bestel vir 'n {k}.", msg_g='Vir hoeveel mense',
           rx_date='bestel|datum|oop|beskikbaar|koek')

HZ = dict(phone='078 861 7650', wa='27788617650', mail='info@hellozara.solutions',
          maps='https://www.google.com/maps/search/?api=1&query=Vanderbijlpark', fb='https://www.facebook.com/hellozara.ai')

FICTION = [
 dict(slug='voorbeeld-lokaal', L=EN2, name='Willow Creek Venue', owner='Anna', they='she', title='Willow Creek Venue · sample website by Hello Zara',
      desc='A sample venue website by Hello Zara: weddings, birthdays and year-end functions.',
      fonts='family=Cormorant+Garamond:ital,wght@0,500;0,600;1,500&family=Great+Vibes&family=Lato:wght@400;700',
      head='"Cormorant Garamond",Georgia,serif', body='"Lato",system-ui,sans-serif', script='"Great Vibes",cursive',
      c=dict(a='#4f6f5a', a2='#3a5443', bg='#f7f4ee', panel='#e8eee7', ink='#2d3530', muted='#5f6b63', line='#d8e0d8', dark='#243029', accent='#e7cfa6', soft='#efe7da'),
      logo=None, brand_line='WEDDINGS & FUNCTIONS · SAMPLE',
      hero=U('photo-1696021922703-022b8c280fb1', 2000), hero_alt='An outdoor ceremony set up between the trees',
      h1='Your big day, <em>under the willows</em>.', lead='A garden venue for weddings, birthdays and year-end functions. Couples can see the open dates and ask about theirs in one minute, any time of day.',
      proof=[('4.8', 'on Google'), ('2027', 'dates now open')],
      events_title='From the ceremony to the last dance.', events_intro='Tell Anna what you are planning. She lets you know if the date is open.',
      events=[('Weddings', 'The ceremony in the garden and the reception in the hall.'), ('Birthdays', 'Big birthdays with the people you love.'), ('Year-end functions', 'Team functions with food, music and space to dance.')],
      kinds=['Wedding', 'Birthday', 'Year-end function', 'Other'],
      avail=[('November', '7 and 28 November'), ('December', '5 and 12 December')], avail_note='Sample dates. On your site these come from your own calendar.',
      gallery=[(U('photo-1665607437981-973dcd6a22bb'), 'The hall set for a reception'), (U('photo-1680695779444-24fc71296e66'), 'A table set for a wedding'), (U('photo-1526092817387-8f07b2904e48'), 'String lights in the gazebo')],
      side=U('photo-1680695627150-e5015d861665', 1200), side_alt='A long table set for a wedding reception',
      quote='Everything was perfect, and we knew within the hour that our date was open.', quote_by='Sample review',
      addr='Vaal Triangle (sample)', a_what='We host weddings, birthdays and year-end functions in the garden and the hall.',
      a_where='This is a sample venue. On your website this shows your own address and a map.',
      a_price='Every event is different, so Anna sends a quote for your date and number of guests. Shall I ask about your date?',
      motif='lights', split=True, **HZ),
 dict(slug='voorbeeld-koek', L=AF2, name='Suikerbossie Koffie & Koek', owner='Marlize', they='sy', title="Suikerbossie Koffie & Koek · voorbeeld-webwerf deur Hello Zara",
      desc="'n Voorbeeld-webwerf vir 'n koekwinkel en koffiewinkel, deur Hello Zara.",
      fonts='family=Pacifico&family=Nunito:wght@400;600;700',
      head='"Nunito",system-ui,sans-serif', body='"Nunito",system-ui,sans-serif', script='"Pacifico",cursive',
      c=dict(a='#c0577a', a2='#9e3f60', bg='#fff8f5', panel='#fbe9ee', ink='#2e2427', muted='#6a5a5f', line='#f1dbe1', dark='#3a2a2f', accent='#f6c9a8', soft='#fdf1e8'),
      logo=None, brand_line='KOFFIE · KOEK · BESTELLINGS',
      hero=U('photo-1606983340126-99ab4feaa64a', 2000), hero_alt="'n Sjokoladekoek met roosversiering",
      h1="Elke koek <em>vir iemand gebak</em>.", lead="Verjaarsdagkoeke, troukoeke en kolwyntjies, en 'n koppie koffie as jy inloer. Bestel in een minuut: dit kom netjies op ons WhatsApp aan.",
      proof=[('4,9', 'op Google'), ('3 dae', 'kennisgewing vir bestellings')],
      events_title='Van kolwyntjies tot troukoeke.', events_intro='Sê vir Marlize waarvoor die koek is. Sy laat weet of die datum oop is en wat dit kos.',
      events=[('Verjaarsdagkoeke', 'Enige tema, enige grootte.'), ('Troukoeke', "Een laag of vyf, met 'n proe-afspraak."), ('Kolwyntjies en bokse', 'Vir die kantoor, die skool of net vir jouself.'), ('Koffie en koek', 'Kom sit by ons in die winkel.')],
      kinds=['Verjaarsdag', 'Troue', 'Kolwyntjies', 'Ander'],
      gallery=[(U('photo-1558301211-0d8c8ddee6ec'), 'Fondant-koek op \'n staander'), (U('photo-1486427944299-d1955d23e34d'), 'Ses kolwyntjies met sprinkels'), (U('photo-1545418314-7ce0b9b53901'), 'Die koffiemasjien en spyskaart')],
      side=U('photo-1621303837174-89787a7d4729', 1200), side_alt="'n Pienk en wit koek op 'n bord",
      quote='Die mooiste koek, en ek moes net een keer vra.', quote_by='Voorbeeld-resensie',
      addr='Vaaldriehoek (voorbeeld)', a_what="Ons bak verjaarsdagkoeke, troukoeke en kolwyntjies, en ons is 'n koffiewinkel waar jy kan kom sit.",
      a_where="Dis 'n voorbeeld-besigheid. Op jou webwerf staan jou eie adres en 'n kaart.",
      a_price="Dit hang af van die grootte en die tema. Marlize stuur vir jou 'n kwotasie. Sal ek jou bestelling neem?",
      motif='flowers', **HZ),
]

_m = runpy.run_path(os.path.join(T, 'more.py'))
for v in FICTION:
    os.makedirs(D + v['slug'], exist_ok=True)
    open(D + v['slug'] + '/index.html', 'w').write(page(v))
    _m['inject'](D + v['slug'] + '/index.html', v['L']['lang'], v['name'], '<footer')
    print('built', v['slug'])

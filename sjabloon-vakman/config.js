/* ============================================================
   VAKMAN-SJABLOON — the only file you change per prospect
   (plus the colours in index.html :root and the photos in img/)

   RULES (hellozara-demo-site skill):
   - Every fact here must come from THEIR Facebook, Google listing or posters.
   - Leave a field empty ("" or []) when you don't know it: the section hides itself.
   - No prices they didn't publish, no stats, no made-up reviews.
   - WhatsApp number: 27 + number without the leading 0.
   ============================================================ */
window.SITE = {
  lang: "en",                       // "en" or "af" — buttons and labels follow this
  demo: true,                       // shows the "demo by Hello Zara" bar
  sample: true,                     // TEMPLATE ONLY: marks the sample business; set false for a real prospect

  name: "Sample Kitchens & Cupboards",
  short: "Sample Kitchens",         // used in the chat header and messages
  owner: "Johan",                   // first name only; Zara says "I'll make sure Johan sees it"
  logo: "",                         // "img/logo.png" — empty shows the name as a wordmark
  tagline: "Kitchens and built-in cupboards, measured, made and fitted by one team.",
  intro: "From the first measure to the last handle, the same people do the work. Send a photo of your space and get a quote.",
  area: "Vanderbijlpark",           // the base town or suburb (home-based: suburb only)
  since: "",                        // e.g. "2009" — only if they state it
  phone: "016 000 0000",
  whatsapp: "27000000000",
  email: "",
  hours: [                          // only what they publish
    ["Mon – Fri", "07:30 – 16:30"],
    ["Saturday", "By appointment"]
  ],
  google: { rating: "", count: "", url: "" },   // e.g. "4.9", "38"
  review: { text: "", name: "" },               // ONE short real Google review, first name only

  hero: { img: "", caption: "Hero photo: their best finished job" },

  services: [
    { name: "Kitchens", text: "New kitchens and full kitchen makeovers." },
    { name: "Built-in cupboards", text: "Bedroom cupboards, walk-in closets and storage." },
    { name: "Bathroom vanities", text: "Vanities and bathroom cabinets made to measure." },
    { name: "Repairs & doors", text: "New doors, hinges and tops on existing cabinets." }
  ],

  work: [                           // real photos of their work; caption = what + where, only if known
    { img: "", caption: "Photo of a finished kitchen" },
    { img: "", caption: "Photo of built-in cupboards" },
    { img: "", caption: "Photo of a vanity or detail" },
    { img: "", caption: "Photo of the team at work" },
    { img: "", caption: "Another finished job" }
  ],

  areas: ["Vanderbijlpark", "Vereeniging", "Three Rivers", "Meyerton", "Sasolburg"],

  steps: [                          // how a job runs — only if they describe it, otherwise []
    { name: "You send photos", text: "WhatsApp a few photos and rough sizes of the space." },
    { name: "We measure", text: "We come out, measure properly and talk through options." },
    { name: "You get a quote", text: "A written quote, so you know exactly what you pay for." },
    { name: "We make and fit", text: "Made to measure and fitted by the same team." }
  ],

  quote: {                          // the quote slip that becomes a WhatsApp message
    when: ["As soon as possible", "Within a month", "In 1 – 3 months", "Just getting prices"],
    note: "Photos help: you can add them in WhatsApp after this message opens."
  },

  /* Extra chat answers, from their own page. Keys are regex words; value is the answer. */
  faq: [
    { q: "guarantee|warranty|waarborg", a: "" },
    { q: "material|board|wood|hout|granite|quartz", a: "" }
  ]
};

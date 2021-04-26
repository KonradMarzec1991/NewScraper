## NewsScraper

---

### Description
Gets news information (headlines) from main boards of 
mainstream media (wp, onet, interia, polsat news).


### How to run
1. `docker-compose up --build`
2. Override `settings.INTERVALS` up to your preferences - default is `0,6,12,18`
3. If you want `ad-hoc` retrieve, POST `127.0.0.1:8000/load/` with `portal` key
4. Available options: `onet`, `wp`, `interia`, `polsatnews`.
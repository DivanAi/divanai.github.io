# DivanAI — yapay zekâlar aynı masada

**Site:** https://divanai.github.io/  ·  **Kaynak:** https://github.com/divanai/divanai.github.io  ·  **Hata/öneri:** https://github.com/divanai/divanai.github.io/issues

**Türkçe** · [English](README.en.md) — arayüz iki dilli: üst şeritteki bayraklarla Türkçe ⇄ İngilizce.

> **Divan**, Osmanlı'da devlet işlerinin görüşüldüğü meclis; **AI** eki onu yapay zekâya taşır.
> Okunuşu: *di-va-na-i*. Doğru yazım: **divanai** (bitişik, tamamı küçük harf).

Bir konu yazıyorsun; masadaki yapay zekâlar sırayla konuşuyor, birbirine itiraz ediyor, en sonunda
başkan toparlayıp özetliyor. Sekmeler arasında kopyala-yapıştır yok.

**Tek dosya.** `index.html`'e çift tıkla, açılır. Kurulum, hesap, sunucu gerekmez.
**Anahtarsız açılır (Demo).** Uygulama **Demo** modunda açılır: üç sandalye üç ayrı ücretsiz servise bağlıdır
(OVH · LLM7 · Pollinations), kayıt yok, anahtar yok. Cevaplar **gerçektir** — hazır/örnek metin değildir;
bedeli yavaşlık ve servislerin günlük kotasıdır. **Canlı** mod ise **API anahtarı ister**: kendi anahtarınla
daha hızlı ve daha yüksek kota; varsayılan masa canlıda **4 sandalye**.

| **Konsey** | **Panel** | **Ayna** | **Ajanlar** | **TekeTek** |
|---|---|---|---|---|
| ![Konsey](ekranlar/1-konsey.jpg) | ![Panel](ekranlar/27-panel.jpg) | ![Ayna](ekranlar/3-ayna.jpg) | ![Ajanlar](ekranlar/11-ajan-kurulum.jpg) | ![TekeTek](ekranlar/26-teketek.jpg) |
| 3–5 ayrı şirketin modeli, roller, başkan özeti | Sandalyeler **aynı anda**, birbirini görmeden yazar; **kıyaslama sende** | Aynı model iki sandalyede: savunan + itiraz eden, hakem kararı | Her sandalyeye ayrı görev, zincirleme teslim, tek teslimat | Tek yapay zekâ, doğrudan cevap; anahtarsız seçenek **yavaş** çalışır |

Tek sohbet istersen **TekeTek**: masada tek yapay zekâ olur, yazdığını doğrudan cevaplar. **Anahtarsız
seçenek hazır gelir** (gpt-oss 20B, Pollinations) — kayıt olmadan gerçek cevap alırsın; yavaş çalışır
(7 Kasım 2026 ölçümü: ilk cevap **22 saniye**, aynı sorunun tekrarı önbellekten 1 saniyenin altında), düzgün deneme için ücretsiz anahtar daha iyidir.

---

## Dürüst sınırlar (özet)

Bunlar reklam değil, ölçüm:

| Konu | Gerçek |
|---|---|
| **"Ücretsiz"** | Uygulama para almaz, hesap istemez, istek saymaz. **Servisler** sınır koyar: OpenRouter `:free` modellerde günde 50 istek (bir tur 4 istek → ~12 tur), Groq ücretsiz katmanda günde 1.000, Pollinations yayınlanmış kota vermez ama yoğunlukta bekletir. |
| **Demo modu (anahtarsız)** | Gerçek cevap, hazır metin değil — ama **görsel okuyamaz** ve yavaştır (ilk cevap 20–60 sn). **Canlı** mod API anahtarı ister. |

![Demo modu: üç anahtarsız servis, gerçek cevaplar](ekranlar/116-demo-gercek-cevap.jpg)
| **Web araması** | Yalnız OpenRouter'da ve **ücretli**: istek başına ~0,7–1,5 sent. Ücretsiz modelde bile kredi harcar. Varsayılan kapalı. |
| **Ayna** | Aynı model iki rolde: kendi kendini onaylamayı zorlaştırır. Modelin **her yerde paylaştığı** kör noktayı yakalamaz — modeli değiştirmenin yerini tutmaz. |
| **Sayı kuralı** | Kaynaksız tutarı `[?]` yapar; cevabı doğru yapmaz. Oranlar da yanlış olabilir, ama tartışılabilir. |
| **Anahtar kilidi** | Kapalıyken anahtar düz metin. Açmak isteğe bağlı; parola unutulursa kurtarma yok. |

---

## Hemen başla (30 saniye)

1. `divanai` klasörünü indir, içindeki **`index.html`**'e çift tıkla. (Python, kurulum, internet gerekmez.)
2. Ekranın üstünden masa türünü seç: **Konsey · Panel · Ayna · Ajanlar · TekeTek**.

**Hiçbir şey ayarlamadan başla.** Uygulama **Demo** modunda açılır ve masaya **üç anahtarsız sandalye** kurar:
**OVH AI Endpoints** (Llama 3.3 70B), **LLM7.io** (Codestral), **Pollinations** (gpt-oss 20B) — üçü ayrı
servis, **kayıt yok, anahtar yok, kart yok**. Cevaplar gerçektir; ilk tur yavaştır (ölçüm: 7 Kasım 2026'da
üç sandalyeli bir tur **~65 saniye**; LLM7 aynı anda tek istek alır, OVH dakikada 2 istek).
**TekeTek** sekmesi de anahtarsız çalışır (Pollinations); orada cevaplar sırayla gelir.
3. Kutuya konuyu yaz ve `Enter`. *(Örnek: "Bursa'da küçük bir kahve dükkânı açmak mantıklı mı?")*
4. Demo modunda **hiçbir anahtar harcanmaz**; ücretsiz servislerin kendi günlük kotası kullanılır. Kota dolarsa
   sandalye tek satır uyarı bırakıp sıradaki ücretsiz servise geçer.

**Daha hızlısı isteğe bağlı (3 adım):** ① ücretsiz bir sağlayıcıda hesap aç — en cömert ücretsiz
katman **Google AI Studio**'da (kart istemez, günlük hak **her model için ayrı**); ② anahtarı kopyala,
③ Ayarlar → **Ücretsiz · kendi anahtarın** → **Google AI Studio** → anahtarı yapıştır → **⇅ Bağlantıyı test et**
→ **Kaydet ve uygula**. Bir bağlantı kartına bastığında o servis **bütün sandalyelere** uygulanır; uygulama
bunu bir bildirimle söyler. Ücretli servisler (**Vercel, Requesty, NanoGPT, AIMLAPI**…) ana listede değil,
**Diğer servisler** başlığının altında katlı durur — kullanmayacaksan hiç açma. Her kartın köşesinde
**kart ister / kart istemez** etiketi yazar.
Anahtar yalnızca **bu tarayıcıda** (`localStorage`) durur; sunucuya, dosyaya, depoya gitmez.

**Canlıda her sandalyeye ayrı model.** Canlıya geçtiğinde masa **4 sandalye** açılır ve sandalyeler
**farklı modellere** dağıtılır — hepsi aynı modeli konuşmaz. Dağıtım iki kaynaktan gelir:
① anahtarı kaydettiğinde uygulama servisin **kendi model listesini** çeker (`/models`), aile çeşitliliğine
bakarak her sandalyeye ayrı kimlik koyar; ② liste alınamazsa bağlantının **doğrulanmış ön ayarları**
sırayla dağıtılır. Havuz sandalyeden küçükse (Google'ın doğrulanmış ön ayarında 2 model var: 3.5 Flash-Lite
+ 3.1 Flash-Lite) sırayla tekrarlanır ve çekmece bunu **yazar**. Her sandalyenin modelini alttaki listeden
**elle değiştirebilirsin**; elle yazdığın kimlik açılışta korunur, otomatik dağıtım üzerine yazmaz.
Yeniden dağıtmak istersen **Her sandalyeye ayrı model dağıt** düğmesine bas.

![Canlı: 4 sandalye, ayrı modeller](ekranlar/116b-model-dagitimi.jpg)

![Ayarlar — üç anahtarsız sandalye](ekranlar/30-ayarlar-sade.jpg)

*Ayarlar böyle açılır: en üstte mod, altında **üç anahtarsız servis** (Pollinations · LLM7.io · OVH),
sonra ücretsiz anahtarlı servisler; ücretliler **Diğer servisler** başlığının altında kapalı durur.*

**Telefonda:** aynı dosya çalışır; arayüz 360 px'e kadar dikey ekrana uyar.

---

## Kullanım

### 1 · Masayı kur

| Ne | Nerede | Not |
|---|---|---|
| **Masa türü** | En üstteki beş düğme | Değiştirirsen mevcut konuşma temizlenir (önce uyarır) |
| **Konu** | Alttaki yazı kutusu | `Enter` başlatır, `Shift+Enter` alt satır |
| **Dosya ekle** | Yazı kutusunun solundaki **ataç** | Görsel · PDF · Word (.docx) · Excel (.xlsx) · PowerPoint (.pptx) · metin/kod. Panodan **Ctrl+V** ile yapıştırmak da olur; sürükle-bırak çalışır. Dosya **her modda** o soruyla birlikte sandalyelere gider |
| **Gündem** | Konunun altındaki çipler | **Fikir üret · Tartış & eleştir · Karar ver** — yalnız Konsey'de; Ayna'da gündem sabittir |
| **Dil** | Üst şeritteki iki bayrak (Türk · İngiliz) | Arayüzün tamamını Türkçe ⇄ İngilizce çevirir; seçim kalıcıdır. Cevaplar ve yazdığın konu çevrilmez |
| **Model** | Ayna ve TekeTek'te listenin yanındaki seçici | TekeTek'te: **Pollinations · anahtarsız** ya da **kendi bağlantın** |
| **Geçmiş** | Üst şeritteki saat simgesi | Bu tarayıcıdaki son 10 konuşma + **favoriler** · aç, devam et, sil |
| **Bir daha gösterme** | Anahtar kartının sağ üstü | “Canlı modeller için 3 adım” kartını kalıcı olarak gizler (ana ekrandaki anahtar istemini kapatır) |

**Konuşma sürerken:**
- Alta **araya not** yazabilirsin — sıradaki konuşmacılar onu görür.
- **Durdur** ile masayı anında kesebilirsin; yazılmış cevaplar silinmez.

### 1b · Geçmiş konuşmalar ve cihaz taşıma

Hesap yok, giriş yok. Buna karşılık konuşmalar kaybolmasın diye üç şey var:

| Ne | Nerede | Ne işe yarar |
|---|---|---|
| **Son oturum** | Kendiliğinden | Sayfayı yenileyince ya da sekmeyi kapatıp açınca konuşma yerinde durur |
| **Geçmiş listesi** | Üst şerit → **saat simgesi** | Bu tarayıcıdaki son **10 konuşma**: tarih, mod, mesaj sayısı. Tıkla → kaldığı yerden devam. `×` ile tek tek, alttaki düğmeyle hepsi silinir |
| **Favoriler** | Satırdaki **yıldız** (☆) | Önemli konuşmayı işaretle: listenin **en başında** ayrı bölümde kalır ve 10’luk sınır onları **silmez** (en fazla 30 favori) |
| **Oturum dosyası** | Aynı panel → **Oturumu dosyaya kaydet / Dosyadan aç** | Başka cihaza taşımak için `.json` dosyası. WhatsApp/Drive/e-posta ile kendine gönder, öbür cihazda aç |

Geçmiş listesi **yalnız o tarayıcının deposunda** durur; sunucuya gitmez, hesap gerekmez. Tarayıcı verilerini
temizlersen liste de gider — bu yüzden önemli konuşmaları **dosyaya kaydet** ya da **Dışa aktar** ile sakla.
Görsellerin kendisi saklanmaz (yer kaplamasın diye); listeden açılan eski konuşmada görsel kutusu “kayboldu”
olarak görünür.

### 2 · Tur bitince

| Düğme | Ne yapar |
|---|---|
| **+ Bir tur daha** | Aynı konuyu derinleştirir; başkan kapanışı yenilenir |
| **Özet çıkar** | Başkan kararı tek kartta: Sonuç · artı/eksi · ilk adım |
| **Dışa aktar** | **Word (.docx)** · **Metin (.txt)** · **Markdown (.md)** — dosya tarayıcıda üretilir |
| **Kopyala** | Tüm masa panoya, markdown olarak |
| **Yeni masa** | Konuşmayı ve duraklatma kaydını temizler |

Masa **otomatik saklanır**: sayfayı yenilesen son oturum geri gelir. Konuşma geçmişi yedeğe girmez;
onu **Dışa aktar** ile alırsın.

### 3 · Ayarlar (kullanım için gerekenler)

**Masadaki modeller**
- Her sandalyeyi açıp kapatabilirsin (en az bir tanesi açık olmalı). DivanAI beş sağlayıcı tanır:
  ChatGPT, Gemini, Claude, Grok, DeepSeek — **beşi birden** açılabilir.
- **Anahtarı yapıştırınca modeller kendiliğinden gelir**: seçtiğin servisin kendi model listesi
  çekilir ve beş sandalyeye o servise ait modeller yerleşir. Elle model kimliği yazmak zorunda değilsin.
  Kendi seçtiğin ve o serviste bulunan bir model varsa **korunur**, üzerine yazılmaz.
- **Başkan**: özeti ve kapanışı yazan sandalye.
- **Ücretsiz modeller** düğmesi: anahtarın gördüğü `:free` modelleri listeler; önce **hangi sandalyeye**
  atayacağını seç, sonra satırdaki **kullan**'a bas. Seçim yapmadan hiçbir sandalye değişmez.
  **+ Yeni sandalye aç** ile masaya olmayan bir sağlayıcıyı eklersin.

**Konuşma ayarları**

| Ayar | Ne işe yarar | Varsayılan |
|---|---|---|
| **Üslup** | Doğal sohbet (kısa cümle, dolgu yok) · Rapor düzeni (Sonuç/Artı/Eksi/İlk adım) · Kısa madde | **Doğal sohbet** |
| **Cevap sınırı** | Konuşmacı başına en fazla kelime (30–500) | 130 |
| **Bağlam** | Masa hafızası (en az token) · Sıkıştırılmış · Tam geçmiş | **Masa hafızası** |
| **En fazla tur** | Tur tavanı (2–20); dolunca masa durur ve özet çıkarır | 6 |
| **Doyunca dur** | Son iki turda yeni fikir gelmezse kendiliğinden durur | Açık |
| **İnternetten bilgi** | Yalnız OpenRouter'da çalışır ve **kredi harcar**; kapalı tutmak ücretsizdir | Kapalı |

**Bağlantı**
Ücretsiz kalmak istiyorsan başlangıç **Google AI Studio**: kredi kartı istemez, Flash ve Flash-Lite
modelleri ücretsiz; günlük istek hakkı **her model için ayrı** sayıldığı için dört sandalyeye dört ayrı
Gemini modeli yazınca dört ayrı kota kullanılır. (Kesin günlük sayılar AI Studio → *Rate limits*
sayfasında yazar; Google bunları ülkeden ülkeye değiştirebiliyor.) Görsel okuyabilir: fotoğraf ekleyebilirsin.
**Z.ai (GLM)** de kartsız: GLM-4.7-Flash ve GLM-4.5-Flash fiyat listesinde *ücretsiz* yazar ve yayınlanmış
istek kotası yoktur (dakikada sınır çıkabilir). **Anahtarsız** iki seçenek daha var: **LLM7.io** (aynı anda
1 istek) ve **OVH AI Endpoints** (dakikada 2 istek) — ikisi de tek sandalyelik, ama kayıt istemez.
Tek anahtarla çok model isteyenler için **OpenRouter** (ücretsiz `:free` modeller, **günde 50 istek**),
hız isteyenler için **Groq** (**günde 1.000 istek** ama dakikada 8 bin token sınırı). Tek sağlayıcı
kullanmak istersen **Groq, DeepSeek, Mistral, xAI, OpenAI** gibi servislerin kendi anahtarıyla doğrudan
bağlanabilirsin. **Cerebras** artık kalıcı ücretsiz katman vermiyor (30 günlük 5 $ deneme kredisi,
doğrulanmış ödeme yöntemi ister). Groq'un ücretsiz modelleri de değişti: **llama-3.1/3.3 modelleri
16 Ağustos 2026'da kaldırıldı**, ön ayar artık `openai/gpt-oss-120b`, `openai/gpt-oss-20b` ve
`qwen/qwen3.8-27b` kullanıyor. Kendi OpenAI uyumlu adresini (LiteLLM, Cloudflare AI Gateway)
**Özel adres** kartına yazabilirsin. Anahtar hiçbir sunucuya gitmez: yalnızca kendi tarayıcında durur.

![Bağlantı testi ve teşhis](ekranlar/10-teshis.jpg)

**⇅ Bağlantıyı test et** her açık sandalyeye tek kelimelik bir istek atar ve sonucu satır satır yazar:
`✕ Claude · 401 invalid api key` (yanlış anahtar), `✕ Grok · 404 model bulunamadı` (yanlış model kimliği),
`429` (kota), CORS (tarayıcı engeli). Bağlantı hatasında **önce bunu çalıştır.**

> **403 "Key limit exceeded"** alıyorsan anahtar geçerli, **harcama limiti** sıfır demektir.
> `openrouter.ai/settings/keys` → anahtar → **Limit**'i artır (kredi eklemek tek başına yetmez).

**Sandalye başına bağlantı.** Her sandalye kendi sağlayıcısını kullanabilir; günlük ücretsiz hak katlanır.
Örnek: ChatGPT → **Google AI Studio** (Gemini 3.8 Flash), Gemini → **Google AI Studio** (Gemini 3.5
Flash-Lite), Claude → **Google AI Studio** (Gemini 3.6 Flash), Grok → **Groq** (1.000/gün). Dördü de
kartsız; üçü Gemini olduğu için üç ayrı model kotası harcar. Kendi bağlantısı olan sandalye 429 alırsa **yalnız o** beklemede kalır; ortak bağlantıda
bütün sandalyeler birlikte bekler (aşağıya bak: *Boşa token harcamamak için*).
Ayarlar → *Masadaki modeller* → satırın altındaki liste. Seçtiğin sandalyede masa ekranında `⛁ Groq`
gibi bir rozet görünür.

![Sandalye başına bağlantı](ekranlar/9-sandalye-baglanti.jpg)

**Günlük istek hakkı.** Alt çubukta `7 / 50` ve `23s 24dk sonra yenilenir` yazar (yeşil: bol, sarı: az,
kırmızı: bitti). Etikete tıkla → kota kutusu açılır. OpenRouter ücretsiz hak **günde 50**, sıfırlanma
**03:00**; Groq **1.000/gün**; Gemini modele göre, **10:00**. Sayaç istek harcamaz.
**Bilinmeyen servislerde saat uydurulmaz:** kota notu "sağlayıcının kendi sıfırlama saatinde" der.

**Kota dolduğunda ne olur.** İki durum var:

- **Her sandalye ayrı serviste** (varsayılan kurulum: Pollinations · LLM7 · OVH): yalnız kota dolan
  sandalye durur, tek satır uyarı yazılır (`Mistral Nemo bugünlük durdu…`). **Masa devam eder** —
  diğer sandalyeler kendi servislerinde konuşur.
- **Aynı anahtarı paylaşan sandalyeler** (tek Google/OpenRouter anahtarı gibi): hepsi aynı havuzdan yer,
  bu yüzden masa olduğu yerde durur ve ekranda yeşil bir düğme belirir:
**▶ Kaldığı yerden devam · 3 konuşmacı**. Hak yenilenince ona bas; **yalnız kalan** sandalyeler çalışır,
baştan üretmez. Siteyi kapatsan da durum hatırlanır. Özet düğmesi kota 0 iken hiç istek atmaz, masadaki
cümlelerden **yerel özet** çıkarır (kartın başlığı: "Yerel özet · model çağrılmadı").

![Kota doldu: yerel özet + devam](ekranlar/18-kota-devam.jpg)

**Yedekleme.** Ayarlar **bu tarayıcıda** durur. *Yedeği indir (.json)* / *Yedekten yükle* ile taşırsın.
Anahtarlar varsayılan olarak dosyaya **yazılmaz**; kutuyu işaretlersen açık metin taşır (ekranda kırmızı
uyarı çıkar). Yedekte anahtar yoksa bu tarayıcıdaki anahtarlar korunur; bozuk dosya seçersen hiçbir şey
değişmez.

![Yedekleme](ekranlar/15-yedekleme.jpg)

**Masa hafızası (varsayılan).** Her sandalye konuşmadan önce bütün geçmişi baştan okumaz. Program eski
turları tek satırlık notlara indirir; modele yalnız **senin ilk sorun + o not + son iki mesaj** gider.
Not sohbet ekranında **görünmez** — yalnız token harcamasını düşürür. Aynı masada harcama kabaca
altıda bire iner: günde 2–3 masa yerine 10–15 masa.

**Boşa token harcamamak için üç kural.** Hepsi Ayarlar → *Token tasarrufu* altında; istemezsen kapatabilirsin.

- **Geçme (açık, Konsey).** 2. turdan sonra söyleyecek yeni bir şeyi olmayan sandalye cevap yazmaz, yalnız `PAS` der.
  1. turda ve turun kapanış konuşmacısında (başkan) geçme yoktur; Ayna ve Ajanlar'da hiç yoktur.
  Masada tek satır görünür: *"Gemini yeni bir nokta görmedi · geçti, cevap yazılmadı."*
- **Sandalye zaman aşımı (120 sn).** Bir sandalye süresi içinde bitiremezse **yalnız o** kesilir, masa
  beklemede kalmaz. Yarıda kalan metin 30 karakterden uzunsa **korunur** ve "yarıda kesildi" etiketiyle masaya konur.
- **Anahtarsız sandalyelerde tavan 60 sn.** Ücretsiz servisler yoğunlukta yavaşlıyor; ayrıca sıraya giren
  servislerde (OVH dakikada 2) **kuyrukta geçen süre zaman aşımına sayılmaz** (en çok 45 sn eklenir).
  Böylece çalışan bir istek, sıra beklediği için kesilmiyor.
- **Yedek model notu tek satırdır.** "yanıt veremedi · yedek model deneniyor…" satırı, iş bitince aynı satır
  güncellenir ("yerine Codestral geçti" ya da "bu turda konuşamadı"); altına ikinci, çelişkili cümle eklenmez.
- **Yalnız düşünme metni.** Bazı modeller (ör. OVH'de Qwen 3.8) ekranda görünen cevap yerine yalnız düşünme
  metni üretir. Uygulama bunu **"cevap vermedi" diye yazmaz**: "görünür cevap üretmedi · yalnız düşünme metni
  geldi" der ve hangi modelin düz cevap verdiğini o servis için söyler.
- **Başkan özet yazamazsa** masa eli boş kalmaz: kart, masadaki son cümlelerden **yerel özet** olarak çıkar
  ("Özet modelle yazılamadı: başkan sandalyesi yanıt vermedi") ve ne olduğu tek satırda yazar.
  Kartın künyesinde başkanın adı değil **"Yerel özet · yalnız yerel"** yazar — yazmadığı metne imza atılmaz.

![Bir sandalye boş yanıt verdi, biri yalnız düşünme metni üretti: her durum tek satırda, masa durmadı](ekranlar/37-sandalye-durumlari.jpg)
- **Sağlayıcı dinlenmesi (1 dk).** 429 ya da "kredi bitti" hatası alan **bağlantı** bu süre boyunca hiç
  denenmez; sandalyede `dinleniyor · 16:19` rozeti çıkar. Hepsi dinleniyorsa masa duraklatılır, süre dolunca
  **▶ Kaldığı yerden devam** ile sürer. **Dinlenmeyi bitir** düğmesi beklemeden açar.

Ortak anahtarda (OpenRouter gibi) 429 **hesap genelidir**: bir sandalye duvara çarparsa aynı bağlantıyı
kullanan bütün sandalyeler dinlenir. Her sandalyeye ayrı bağlantı verirsen her biri kendi hakkını harcar.

**Hangi masada geçerli?** Zaman aşımı ve dinlenme **üç masa türünde de** çalışır (Ajanlar'da da zincir
asılı kalmaz, dinlenen bağlantının adımı atlanır). Geçme yalnız **Konsey**'de vardır. Günlük kota ise
dinlenme yaratmaz — 5 dakika bekleme onu çözmez; onun için duraklatma ve **Kaldığı yerden devam** var.
Devam düğmesi açık bir müdahaledir: dinlenme beklemesi varsa onu da kaldırır.

![Token tasarrufu ayarları](ekranlar/23-token-tasarrufu.jpg)

![Bütün sandalyeler dinleniyor: masa duraklatıldı](ekranlar/24-dinlenme.jpg)

---

## Dosya ve görsel yükleme

![Dosya ekleme: tepside PDF, görsel ve Excel](ekranlar/28-dosya-ekleme.jpg)

Yazı kutusunun solundaki **ataç** düğmesiyle (ya da **Ctrl+V** / sürükle-bırak) soruya dosya ekleyebilirsin.
Dosya seçtiğinde kutunun üstünde küçük bir **tepsi** çıkar: adı, boyutu, kaç sayfa olduğu ve ✕ düğmesi
görünür. `Enter`'a bastığında dosya o soruyla birlikte **masadaki bütün sandalyelere** gider; hepsi aynı
belgeyi okur.

| Dosya | Ne olur |
|---|---|
| **Görsel** (png · jpg · webp · heic dışı tüm yaygın türler) | Uzun kenarı 896 px'e küçültülür, modele **görsel olarak** gider. Yalnız görsel okuyabilen modeller yorumlar (OpenRouter üzerinden GPT, Gemini, Claude, Grok ailesinin çoğu). **Anahtarsız seçenek görsel okuyamaz** (ölçüldü: 400 döndürüyor); uygulama görseli göndermez, tek satır uyarı yazar ve belgedeki yazıyla devam eder. |
| **PDF** | İçindeki **seçilebilir yazı** çıkarılır (tarayıcıda, eklenti yok). Taranmış PDF'te yazı yoksa uygulama bunu söyler: sayfanın ekran görüntüsünü yükle. |
| **Word (.docx)** | Paragraflar ve tablolar metne çevrilir. |
| **Excel (.xlsx)** | Sayfa sayfa, hücreler **sekmeyle ayrılmış** metne çevrilir. |
| **PowerPoint (.pptx)** | Slayt slayt metin çıkarılır. |
| **Metin / kod** (.txt · .md · .csv · .json · .html · .js · .py …) | Olduğu gibi eklenir; HTML'in etiketleri temizlenir. |

Görseli olmayan bir bağlantıda (ya da model görsel kabul etmiyorsa) uygulama bunu fark eder: görselleri
çıkarıp isteği **bir kez** yineler, tek satır uyarı gösterir ve o bağlantıya bir daha görsel göndermez. Belge
metni her durumda gider.

Sınırlar: tek dosya **25 MB**, bir mesajda **6 dosya**, belge başına **24 bin karakter** (uzunsa başı alınır
ve uygulama söyler). Dosyalar **senin tarayıcında** okunur; hiçbir yere yüklenmez — yalnız seçtiğin model
sağlayıcısına, istek gövdesinde gider. Görsel her turda yeniden gönderilmez: geldiği mesajda ve **bir
sonraki** mesajda modele taşınır, sonra metinde anılır — böylece token iki katına çıkmaz.

## Panel

![Panel: dört sandalye aynı anda, birbirini görmeden](ekranlar/27-panel.jpg)

Sandalyeler **aynı anda** cevap verir ve **birbirini görmez**: her sandalye yalnız senin sorularını ve
**kendi** önceki cevaplarını görür. Başkan, özet ve hakem yoktur — dört görüş alt alta yazılır,
**karşılaştırmayı sen yaparsın**. Aynı soruya dört farklı modelin ne dediğini tarafsız görmek istediğinde
bunu seç. Her mesaj, sandalye sayısı kadar istek harcar (4 sandalye = 4 istek) ve dört cevap **tek seferde**
gelir; sırayla beklemezsin.

## Konsey

![Konsey konuşması](ekranlar/2-konsey-konusma.jpg)

3–5 ayrı model aynı masada; her birinin bir rolü var, son sözü başkan söyler.

| Sandalye | Rol | Ne yapar |
|---|---|---|
| ChatGPT | **Moderatör** | Masayı açar, tartışmayı yönetir |
| Gemini | **Analist** | Konuyu katmanlara ayırır, ölçüt ve varsayımları belirler |
| Claude | **Eleştirmen** | Zayıf noktaları, riskleri, gizli maliyetleri işaretler |
| Grok | **Mühendis** | Uygulanabilirlik, adımlar, süre |
| DeepSeek | **Araştırmacı** | Veri, örnek, karşılaştırma (varsayılan kapalı) |
| Biri | **Başkan** | Son sözü söyler, özeti yazar |

Roller yapışkan değil: modelleri açıp kapatabilir, başkanı değiştirebilir, rolleri yazabilirsin.
Başlık da ayara uyar — 5 sandalye açtığında "Beş yapay zekâ, tek masa" yazar.

![Beş sandalye](ekranlar/19-bes-sandalye.jpg)

**Her konuşmacı için üç kural** (sistem talimatına gömülü): **kısa** (süsleme, giriş cümlesi yok),
**objektif** (uydurma sayı/fiyat yasak, veri yoksa "kanıt yok"), **tekrar yok** (masada söylenenin
tekrarı ve "X şunu dedi" kalıbı yasak). Yeni bir şey yoksa açıkça söyler.

---

## TekeTek

![TekeTek · anahtarsız](ekranlar/26-teketek.jpg)

Masada tek yapay zekâ var; tartışma, sıra, başkan yok. Yazdığını doğrudan cevaplar, yazmaya devam
ettikçe sohbetin hafızası açık kalır. İki seçenek var:

| Seçenek | Ne gerekir | Ne zaman |
|---|---|---|
| **Pollinations · anahtarsız** | Hiçbir şey — kayıt ve anahtar yok | İlk deneme, tek soru-cevap, ücretsiz kullanım |
| **Kendi bağlantım** | Ayarlar → Bağlantı'da bir sağlayıcı + anahtar | Zaten anahtarın varsa, sınır istemiyorsan |

**Anahtarsız seçeneğin sınırı:** Pollinations yayınlanmış bir kota vermiyor; yoğunlukta isteği bekletiyor
(7 Kasım 2026 ölçümü: ilk cevap 22 saniye, önbellekte 1 saniyenin altı; yoğunlukta 60 saniyeyi aşabilir). Sunucu 402 dönerse uygulama kaç saniye bekleneceğini söyleyip bir kez
kendisi tekrar dener — boş hata ekranı görmezsin.
Sunucu “en iyi çaba” ile çalışır; ara ara yavaşlayabilir. Modelin **iç konuşması (reasoning)** ekrana basılmaz,
yalnız cevabı görürsün. Sohbetin bir yere kaydedilmez; anahtar kullanılmadığı için kaybedilecek bir şey de yok.

---

## Ayna

Tek model iki sandalyeye oturur: **A savunur, B itiraz eder**. İlk turda A açar, ikinci turda **B açar,
A itiraz eder** — biri sürekli savunmada kalmaz. Sonunda aynı model **tarafsız hakem** rolünde karar yazar:
hangi taraf hangi noktada haklı, savunmanın ve itirazın en güçlü 2'şer argümanı, karar verilemeyen nokta
ve onu çözecek veri, ilk adım.

- **+ Bir tur daha**: yeni tur oynanır, karar yenilenir (eski karar kartı silinir).
- Ayna'da **gündem seçilmez** — her zaman *tartış & eleştir*.
- Maliyet: **2 tur + karar = 5 istek** (tek model).

![Ayna · hakem kararı](ekranlar/4-ayna-hakem.jpg)

---

## Ajanlar

Konsey ve Ayna bir soruyu **tartışır**; Ajanlar bir projeyi **yapar**.

1. **Projeyi** yaz (tek cümle): *"Küçük bir el yapımı sabun markası için 6 haftalık lansman planı çıkar."*
2. Her sandalyeye **Görev** ve **Beklenen çıktı** yaz. İkincisi kabul kriteridir. Boş bıraktığın ajan atlanır.
3. **Akışı** seç (aşağıdaki tablo).
4. Gönder. Ajanlar sırayla çalışır, her adım ekranda görünür (**1 ✓ 2 ● 3 · 4 ·**).
5. Sonunda **EKİP TESLİMİ** kartı çıkar: özet, kim ne yaptı, asıl çıktı, açık kalanlar, ilk adım.
6. Yetmezse **+ Bir geçiş daha**: ajanlar bu kez önceki geçişin açık maddelerini kapatmaya çalışır.

| Akış | Ne yapar | İstek |
|---|---|---|
| **Sıralı** (varsayılan) | 1 → 2 → 3 → 4; her ajan öncekinin teslim paketini alır | 4 ajan + birleştirme = **5** |
| **Denetçi** | Başkan önce işi parçalara böler, ajanlar plana göre çalışır, başkan birleştirir | **6** |
| **Karşılıklı devir** | Her ajan bitince sıradakini kendi seçer; "BİTTİ" derse durur | tavan **8** |

**Kaç ajan çalışsın (2…5).** Kurulumun sağ üstünde **Ajan sayısı** seçicisi: `2` · `3` · `4 (hepsi)`.
Yalnız **daraltır** — ilk N açık sandalye çalışır, kadro silinmez; üstteki **≈ N istek** tahmini düşer.
**＋ DeepSeek'i ekle** düğmesi tek tıkla beşinci sandalyeyi açar.

![Ajan sayısı](ekranlar/17-ajan-sayi.jpg)

**Her adımda dur.** İşaretlersen her ajandan sonra **Devam**'a basman gerekir; yanlış giden zinciri
yarıda kesebilirsin. **Geçiş: 1 / 2 / 3** ile aynı kadroyu birkaç kez koşturabilirsin.

**Hazır kadro.** Her sandalye kartının sağ üstünde **Kadro** düğmesi: **12 Türkçe şablon** +
**268 İngilizce uzman kaydı**. Arama iki dilde çalışır (`finans` → hem *Finansal analist* hem *finance*).
Seçim **yalnız o sandalyeye** yazılır: rol + görev + beklenen çıktı. Dolu sandalyede onay ister.

![Hazır kadro](ekranlar/16-kadro.jpg)

**Teslim paketi.** Her ajan cevabının sonuna yapılandırılmış bir paket ekler (AMAÇ · YERLEŞEN · AÇIK ·
KANIT · KISIT · SINIR · SONRAKİ). Sıradaki ajan bütün konuşmayı değil **yalnız bu paketi** görür:
zincir boyunca maliyet karesel büyümez, kısıtlar kaybolmaz.

**Sıfırlama.** Kurulumdaki **✦ Temizle** görevleri, proje cümlesini ve konuşmayı temizler.

**Demo modunda** da cevaplar gerçektir (üç ücretsiz servis); yalnız anahtar harcanmaz, hız ve kota servislerin
kendi sınırına bağlıdır.

---

## Görseller (Ajanlar)

Kurulumda sandalye kartının altındaki **"Bu ajanın metninden görsel çizilsin"** kutusunu işaretle;
o ajan metnini bitirdikten sonra bir görsel çizilir. Hazır projelerde bu kutu **Dergi sayısı** (kapak),
**Restoran açılışı** (vitrin) ve **Ürün lansmanı** (kampanya görseli) için önceden işaretlidir.

> **Görseli ajanın kendisi çizmez.** ChatGPT/Gemini/Claude/Grok metin üretir; görseli seçili
> **görsel motoru** çizer. Ajan yalnız istemi yazar (cevabındaki `GÖRSEL İSTEMİ:` satırı; yoksa devir
> paketindeki *AMAÇ*, o da yoksa cevabın ilk 260 karakteri).

| Motor | Anahtar | Ücret | Sınır | Not |
|---|---|---|---|---|
| **Ücretsiz** (varsayılan) | Gerekmez | **0** | IP başına **45 saniyede 1 görsel** | Sağ altta küçük `pollinations.ai` filigranı; yazı/harf üretmekte zayıf, uzun kenar 1024 px |
| **OpenRouter** | Kendi anahtarın | Görsel başına ~**$0.001–0.003** | Sağlayıcının sınırı | Filigran yok, kalite yüksek; **her oturumda bir kez onay ister** |

**Oran.** GÖRSEL satırında 6 düğme: `1:1` kare · `4:3` kart · `3:2` foto · `16:9` geniş · `9:16` dikey ·
`21:9` sinema. Seçim kalıcıdır ve kartın başlığında etiket olarak görünür. Kartta yazan boyut gerçekten
istenen boyuttur (ücretsiz motor uzun kenarı 1024'te tutar, DivanAI buna göre indirir).

**Kamera etiketleri.** `Sabah ışığı · Portre · Geniş açı · Ürün çekimi · Sinematik · Düz çizim` — görsel
isteminin **sonuna metin ekler**; kredi harcamaz, model değiştirmez. Tekrar basınca kapanır, istemde zaten
geçen parçayı ikinci kez yazmaz.

![Görsel oranı ve kamera etiketi](ekranlar/22-gorsel-oran.jpg)

**Davranışlar**
- Görsel **ayrı bir istek**tir; ajan sohbeti sayılmaz. "≈ 5 istek · 1 görsel (ücretsiz)" gibi yazar.
- Canlı modda, başlamadan önce kaç görsel çizileceği ve hangi motorun kullanılacağı **sorulur**;
  reddedersen metin kısmı yine tamamlanır.
- **Demo modunda hazır görsel üretimi çalışmaz** (anahtar yok). Tek tek denemek için cevabın başındaki
  **Görsel üret** düğmesini kullan; istem yazılırken görsel motoru için anahtar gerekir.
- Hız sınırında kart **"Görsel sırada · N sn"** diye geri sayar. Sunucu dolu dönerse (503) DivanAI 6 saniye
  sonra **bir kez** yeniden dener.
- **Görseller saklanmaz** (tarayıcı kotasını doldurmasın diye). Sayfayı yenilersen resim kaybolur,
  "Yeniden üret" ile geri gelir. Dışa aktarımda resim değil, **istemi** yazılır.

![Görsel üretimi](ekranlar/14-gorsel-uretim.jpg)

---

## Dil

**Arayüz iki dilli: Türkçe ve İngilizce.** Üst şeritteki iki bayraktan birine bas; bütün yazılar
o dile döner — düğmeler, yardım, ayarlar, uyarılar, onay kutuları, dışa aktarma başlıkları. Seçim
tarayıcıda saklanır, sayfayı yenileyince korunur. İlk açılışta tarayıcının dili Türkçe değilse
arayüz İngilizce açılır.

Cevaplar **senin yazdığın dilde** gelir: Türkçe yazarsan Türkçe, İngilizce yazarsan İngilizce.
Uygulama konunun dilini algılar ve her modelin talimatına ekler.

**Çevrilmeyenler:** yazdığın konu, sohbet balonları ve model cevapları. Bunlar sana aittir,
arayüz dili ne olursa olsun olduğu gibi kalır. Demo da Canlı da aynı kurala uyar: model cevabı, konuyu
hangi dilde yazdıysan o dilde gelir.

---

## Sayı kuralı — model fiyat uydurmaz

Fiyat, tutar, maliyet, ciro, kira için **mutlak sayı yazılmaz.** Bu bir temenni değil, kodda uygulanır:

| Katman | Ne yapar |
|---|---|
| **İstem** | Modele "TL / ₺ / $ tutarı yazma; oran, eşik, formül yaz; girdi gerekiyorsa `[kira]` diye boşluk bırak" talimatı gider |
| **Denetim** | Her cevapta sayı + birim aranır (`5.000 TL`, `26 fincan`, `45 m²`). Senin yazdığın sayılar ve varsa kaynaklar **muaf** |
| **Onarım** | Kaynaksız tutar `[?]` yapılır, balonun altına not düşülür: *"2 kaynaksız tutar gizlendi → [?]"*. **İkinci model çağrısı yok** |

**Serbest:** oran (`kira cironun %8–12'si`), formül (`fincan/gün = ciro ÷ sepet ÷ 30`), süre (6 ay), yıl (2026),
uygulamanın kendi bilgisi (3 model, 2 tur), senin verdiğin sayılar.
**Yasak:** uydurulmuş tutar ve uydurulmuş oran ("%37 kira/ciro" gibi).

Ayarlar ▸ **Masa düzeni** ▸ *Sayı kuralı* — varsayılan **açık**. Kapatırsan denetim susar.

> Neden: model fiyat **bilmez**, yapı **bilir**. Fiyatı sen getirirsin, hesabı uygulama yapar,
> oranı model verir — gerekçesiyle ve tartışılabilir olarak.

---

## Geçmişte arama · anahtar kilidi

**Geçmişte arama.** Üst şeritteki saat simgesi geçmiş listesini açar; üstündeki kutuya yazdığın anda
liste süzülür. Konu başlığı, masa türü, tarih ve konuşma metni içinde arar. `Esc` aramayı temizler.

**Anahtar kilidi (isteğe bağlı).** Anahtarlar normalde bu tarayıcının yerel deposunda **düz metin**
durur — tarayıcı verisini okuyan biri görebilir. Ayarlar → Bağlantı bölümündeki kutudan bir **parola**
belirlersen anahtarlar **PBKDF2 (150.000 tur) + AES-GCM-256** ile şifrelenir ve depoda yalnız şifreli
kutu kalır. Kilit her açılışta kapanır; parolayı sen girersin. **Parolayı unutursan anahtarlar
kurtarılamaz** — başka yerde bir kopyası olsun. Kaldırmak tek düğme.

---

## Görünüm · gündüz ve gece

İki tema var, düzeni hiç değiştirmez — yalnız renkler ve başlık yazısı değişir.

| | **Gündüz (varsayılan)** | **Gece** |
|---|---|---|
| Zemin | kâğıt `#f6f2ea` | gece `#08090d` |
| Mürekkep | `#1b1a17` | `#eef1f7` |
| Vurgu | kehribar `#8a5a2b` | sarı `#f5c76a` |
| Başlıklar | serif (Georgia) | sans-serif |

Üst şeritteki **tek simge** ile geçilir: gündüzde ay, gecede güneş görünür (simge gidilecek
modu gösterir). Seçim tarayıcıda saklanır; ilk açılış **gündüzdür**. `G` tuşu da değiştirir
(yazı kutusunda çalışmaz). Ayarlar çekmecesinde de `☀ Gündüz / ☾ Gece` satırı vardır.

Marka artık sayfadan ayrı duran bir **plaka**: krem-pirinç zemin, çift çerçeve, üstte ince pirinç çizgi.
Plakaya **tıklayınca ana ekrana dönersin**; masada konuşma varsa önce sorar, konuşma sürerken hiç
dokunmaz (önce “Durdur”). Klavyeyle de çalışır: plaka bir düğmedir, `Tab` ile odaklanıp `Enter` ile basılır.

| Plaka · gündüz | Plaka · gece |
|---|---|
| ![Plaka gündüz](ekranlar/118-logo-gunduz.jpg) | ![Plaka gece](ekranlar/118-logo-gece.jpg) |

Kontrast WCAG AA üstündedir: gövde 15,6 · ikincil 8,4 · soluk 6,0 · buton yazısı 5,8.
`prefers-reduced-motion` açıksa geçiş animasyonu kapanır.

---

## Paylaş · bağlantı ve sohbet özeti

Konuşma bittiğinde yazı kutusunun üstünde **Dışa aktar · Paylaş · Kopyala** düğmeleri çıkar.
**Paylaş** iki iş yapar: sayfanın **adresini** paylaşır, istersen **sohbetin özetini** de yanına katar.

| Nerede | Ne zaman görünür |
|---|---|
| Alt çubuk, Dışa aktar ile Kopyala arasında | Masada konuşma olduğunda (Dışa aktar ve Kopyala ile aynı kural) |

| Ne paylaşılır | Nereye | Ne gider |
|---|---|---|
| **Bağlantı** | WhatsApp · Telegram · X · Facebook · LinkedIn · E-posta | Yalnız adres + **tek satır başlık** (“DivanAI — yapay zekâlar aynı masada”). Kartta başlık, açıklama ve önizleme görseli (og etiketleri) çıkar |
| **Sohbet özeti** | Kopyala · WhatsApp · E-posta · cihazın paylaş menüsü | Konu (ilk 200 karakter), her sandalyenin cevabı (ilk 220 karakter), varsa başkan özeti (ilk 320 karakter) ve adres — **en fazla 1 500 karakter** |

Özet **cihazda** üretilir; hiçbir sunucuya gitmez. Sohbetin tamamı adrese gömülmez: uzun bir
konuşma on binlerce karakterlik bağlantı olur ve çoğu uygulama onu keser. Tam metin için
**Dışa aktar** (Word · Metin · Markdown) var.

Yerelde açtığında (`localhost`) paylaş düğmesi kendi bilgisayarının adresini değil, sayfadaki
`canonical` adresi verir — çünkü `localhost` başkasında açılmaz.

| Paylaş düğmesi: Dışa aktar · Paylaş · Kopyala | Paylaş penceresi (Türkçe) |
|---|---|
| ![Düğme](ekranlar/117-paylas-dugme.jpg) | ![Paylaş](ekranlar/117-paylas.jpg) |

| İngilizce | Telefon |
|---|---|
| ![Share](ekranlar/117-paylas-en.jpg) | ![Mobil](ekranlar/117-paylas-mobil.jpg) |

---

## Telefona kur (uygulama gibi)

Site bir **PWA**'dır. Chrome/Edge'de adres çubuğundaki **Kur** düğmesiyle, iPhone/iPad'de
**Paylaş → Ana Ekrana Ekle** ile kurulur. Kurulunca tam ekran açılır ve ilk açılıştan sonra
**internet olmadan da** açılır: service worker son sürümü önbelleğe alır, internet varken her
zaman taze sürümü çeker (eski sürüm takılı kalmaz).

- Kurulum düğmesi **yalnız site adresinden** (https) çalışır. `index.html` dosyasını çift
  tıklayıp açtığında tarayıcı kurulum sunmaz; uygulama yine normal çalışır.
- Paketin yanında **4 küçük dosya** durur: `manifest.json`, `sw.js`, `icon-192.png`, `icon-512.png`.
  Uygulamanın kendisi yine tek dosyadır (`index.html`); bu dört dosya olmadan da açılır,
  yalnız kurulum ve çevrimdışı açılış çalışmaz.
- “Cihazda paylaş” düğmesi yalnız bu özelliği destekleyen tarayıcılarda görünür.

---

## Veri nerede?

Kısa cevap: **sende kalır.** DivanAI'nın kendi sunucusu, hesabı, veritabanı yoktur.

| Ne | Nerede durur | Kim görebilir |
|---|---|---|
| API anahtarın | Yalnızca **senin tarayıcının** `localStorage`'ında | Sen. Hiçbir sunucuya gönderilmez; sayfayı barındıran GitHub da göremez |
| Ayarların (modeller, roller, üslup, tur sayısı) | Aynı yerde, tarayıcında | Sen |
| Son konuşma | Tarayıcı oturumunda; sayfayı yenilersen geri gelir | Sen |
| Yazdığın konu ve metinler | **Seçtiğin sağlayıcıya** (OpenRouter, Groq, OpenAI…) istek olarak gider | O sağlayıcı, kendi gizlilik politikasına göre |
| Dosyaya kaydettiğin `.md` çıktısı | Kendi bilgisayarında, indirdiğin yerde | Sen |
| Çerez, izleme, reklam | **Yok** | — |

> Anahtar tarayıcında durur: ortak kullanılan bir bilgisayarda DivanAI'yı açarken **Demo** modunu kullan (anahtar hiç devreye girmez) ya da anahtarları parolayla kilitle.
> Anahtarı verdiysen Ayarlar → anahtar alanını boşalt → **Kaydet**; anahtar tarayıcıdan silinir.

**Silmek istersen:** Ayarlar'da anahtar alanını boşalt ve Kaydet (anahtar gider), ya da tarayıcıdan
bu sayfanın site verilerini sil (ayarlar da gider). Sunucuda silinecek bir şey yoktur, çünkü sunucuda
hiçbir şey tutulmaz.

**Ajan modunda görevler** yalnızca açık oturum boyunca tutulur; sayfayı kapatınca biter. İstersen
menüden yedek al: yedek dosyası bilgisayarına iner, oradan da sana ait.

---

## Takıldığında

| Belirti | Ne yapmalı |
|---|---|
| "… bugünlük durdu (günlük kota doldu)" | **Yalnız o sandalye** durur; diğer sandalyeler kendi servislerinde konuşmaya devam eder. Aynı anahtarı paylaşan sandalyeler varsa masa **▶ Kaldığı yerden devam** ile bekler |
| `401 invalid api key` | Anahtar yanlış: Ayarlar'da yeniden yapıştır, **⇅ Bağlantıyı test et** |
| `404 model bulunamadı` | Model kimliği yanlış: satırdaki kimliği düzelt (her serviste farklıdır) |
| `403 Key limit exceeded` | Anahtarın **harcama limiti** sıfır: `openrouter.ai/settings/keys` → Limit'i artır |
| Sandalye sessiz kaldı | DivanAI yedeğe geçer ve cevabın başlığında `↺ model` yazar; tur durmaz |
| Cevap yarıda kesildi | Bir kez kendiliğinden yeniden denenir; sürerse Ayarlar'dan kelime sınırını düşür ya da daha küçük model seç |
| Görsel gelmedi | Hız sınırı (45 sn) ya da sunucu dolu (503); karttaki **Yeniden dene**'ye bas |
| Boş/tekrar eden cevap | Ücretsiz modeller yoğun olur; başka bir ücretsiz model dene ya da ücretli modele geç |
| Masa çok uzun sürüyor | **Durdur**, **En fazla tur**'u düşür, **Doyunca dur** açık kalsın |
| Ayarlar kayboldu | Tarayıcı verisi silinmiş: **Yedekten yükle** (anahtarlar ayrıca girilir) |

---

## Ücretsiz servisler · 6 Kasım 2026 ölçümü

Varsayılan kurulum **anahtarsız** üç servisle çalışır. Hangisinin ne yaptığını tahmin etmek
yerine ölçtüm — sonuçlar aşağıda. Ölçüm: aynı soru, tek istek, akış açık, 6 Kasım 2026.

| Servis | Model | Süre | Sonuç |
|---|---|---|---|
| OVH AI Endpoints | Llama 3.3 70B | 0,7 sn | düzgün cevap |
| OVH AI Endpoints | Mistral Small 3.2 | 2,4 sn | düzgün cevap |
| LLM7.io | Codestral | 0,8–1,0 sn | düzgün cevap — **günlük kota dolunca 429** (sunucu: "yeniden deneme 24 saat") |
| Pollinations | gpt-oss 20B | 6 sn – 45 sn | düşünen model; yoğunlukta görünür metin hiç gelmiyor |
| OVH AI Endpoints | Qwen 3.8 27B | 51 sn | **boş** — yalnız düşünme metni, listeden çıkarıldı |
| LLM7.io | Mistral Nemo | 5,7 sn | **bozuk Türkçe** (cümle ortasında yabancı kelimeler), çıkarıldı |

Bu yüzden 6 Kasım'da şunlar değişti:

- **Bozuk modeller listeden çıktı.** Mistral Nemo (LLM7) ve Qwen 3.8 (OVH) artık ön ayarlarda
  yok. Kayıtlı ayarında bu kimlikler varsa açılışta **kendiliğinden** Codestral / Llama 3.3'e
  çevrilir — elle bir şey yapman gerekmez.
- **Sıra hıza göre.** İlk sandalye ve başkan artık **OVH Llama 3.3** (0,7 sn); LLM7 ikinci,
  Pollinations üçüncü (en yavaş, yalnız yedek).
- **Düşünen model tuzağı kesildi.** Bir model 12 saniye boyunca yalnız "düşünme" metni üretip
  görünür cevaba geçmezse o deneme kesilir, sıradaki ücretsiz servis devralır. Eskiden 60 saniye
  boş bekliyordu ("60 sn içinde cevap vermedi" satırı buydu).
- **Yedek zinciri artık servis değiştiriyor.** Bir servis 400/429/boş yanıt dönerse sandalye
  önce aynı serviste başka modeli, sonra **anahtarsız diğer servisi** dener (LLM7 → OVH →
  Pollinations). Önceden aynı servisin içinde kalıp boş dönüyordu.
- **Not yer değiştirdi.** "Mistral Nemo yanıt veremedi · yerine Codestral geçti" satırı artık
  cevabın **üstünde** duruyor; eskiden altında kalıp cevabın kendisi sanılıyordu.
- **Yanlış model adı kendi kendini onarıyor.** Bir sağlayıcı "model bulunamadı" (404) derse
  uygulama o servisin `/models` listesini sorar, çalışan bir kimlik seçer, kaydeder ve cevabı
  alır. Ön ayardaki bir isim yarın eskise bile masa kilitlenmez.
- **Ayarlar dürüst konuşuyor.** Anahtarsız görünümün altında 429/boş yanıt uyarısı ve her
  anahtarsız servisin **ölçülmüş** notu var (hız, sınır, hangi model çalışıyor).

![Anahtarsız uyarı](ekranlar/38-anahtarsiz-uyari.jpg)

### Daha akıcı olmasını istersen: kartsız ücretsiz anahtar

Anahtarsız servisler "en iyi çaba" ile çalışır: bedava oldukları için yoğunlukta bekletirler.
Kesintisiz çalışması için **tek bir kartsız anahtar** yeterli. Ölçülen/toplanan seçenekler:

| Servis | Kart | Sınır (kaynak) | Not |
|---|---|---|---|
| **Google AI Studio** (Gemini) | istemez | Model başına sınır **AI Studio → Rate limits** ekranında görünür; topluluk ölçümü Flash sınıfı için ≈ günde 500 istek, dakikada 15–30 (Ekim 2026) | Türkiye'de ücretsiz katman açık; görsel/PDF okuyor. Türkiye'de en kolay ve en geniş seçenek. |
| **Groq** | istemez | günde ≈1.000 istek, dakikada ≈30, dakikada 6–8 bin token (topluluk takibi) | Çok hızlı; uzun cevaplarda token sınırına takılır. |
| **Cloudflare Workers AI** | istemez (hesap) | günde 10.000 neuron (Cloudflare duyurusu) | Küçük modeller; OpenAI uyumlu adres. |
| **Z.ai (GLM)** | istemez | GLM-4.7-Flash ücretsiz havuz | Kotasız deniyor; doğrulamak için hesap gerekir. |
| **Mistral** | istemez (telefon doğrulaması) | "Experiment" ücretsiz katman | Sınırlar hesap ekranında. |
| **Cohere** | istemez | deneme: ayda 1.000 istek | Deneme kotası; uzun vadeli değil. |

**Öneri:** sırayla **Google AI Studio** → **Groq**. İkisi de kart istemez; Ayarlar → Bağlantı
ekranından anahtarı yapıştırınca bütün sandalyeler o servise geçer. Hiçbiri zorunlu değil:
anahtarsız kurulum da çalışır, yalnız bazen 20–60 saniye bekletir.

## Bilinen sınırlar

- **Demo da gerçek modeldir; bedeli yavaşlık ve kotadır.** Üç ücretsiz servis (OVH · LLM7 · Pollinations)
  anahtarsız cevap verir; hazır metin yoktur. Günlük kota dolunca o sandalye yedeğe düşer.
- **Canlı mod API anahtarı ister ve internet ister.** Anahtar yoksa canlı masa çalışmaz; denemek için Demo var.
- **Kısalık bir üst sınırdır.** Model sınırı aşmaz ama bazen gereğinden kısa yazabilir; uzun analiz için
  tek konuya odaklanmış yeni bir masa aç.
- **En fazla 5 sandalye** — DivanAI beş sağlayıcı tanır. Aynı sağlayıcıyı ikinci sandalyede kullanmak
  (ör. iki farklı GPT modeli) bugün mümkün değil.
- **Görseller sayfa yenilenince kaybolur**; konuşma metni ve istemleri kalır.
- **Yedek cihazlar arası otomatik eşitlenmez** (hesap/sunucu yok, bilerek).
- **Telefona kurulum yalnız site adresinden** (https) çalışır; `index.html` dosyasını çift tıklayıp
  açtığında kurulum düğmesi çıkmaz, uygulama yine normal açılır.

---

## Ekranlar

| Mobil · Ayna | Günlük istek hakkı |
|---|---|
| ![Mobil](ekranlar/5-mobil.jpg) | ![Kota](ekranlar/7-kota.jpg) |

| Ajanlar · akış ve teslimat | Ayna: gündem seçeneği yok |
|---|---|
| ![Akış](ekranlar/12-ajan-akis.jpg) | ![Ayna](ekranlar/20-ayna-gundem.jpg) |

| Görsel kutusu: ajanın metninden çizilir | Bağlantı ayarları: kart istemez / kart ister |
|---|---|
| ![Görsel kutusu](ekranlar/21-gorsel-kutusu.jpg) | ![Bağlantı](ekranlar/8-baglanti.jpg) |

| Ücretli servisler ayrı katmanda | Sandalye başına bağlantı |
|---|---|
| ![Diğer servisler](ekranlar/25-diger-servisler.jpg) | ![Sandalye bağlantısı](ekranlar/9-sandalye-baglanti.jpg) |

| Anahtarsız uyarı ve ölçülmüş servis notları (6 Kasım 2026) |
|---|
| ![Anahtarsız uyarı](ekranlar/38-anahtarsiz-uyari.jpg) |

*DivanAI · tek dosya · dışa bağımlılık yok.*

---

## Lisans

**Apache License 2.0** — tam metin: `LICENSE`, atıf bildirimi: `NOTICE`.
Kod ücretsizdir; gelir yalnız gönüllü bağışla. Ajanlar modundaki 268 İngilizce uzman kaydı
[agency-agents](https://github.com/msitarzewski/agency-agents) projesinden (MIT) alınmıştır; ayrıntı `NOTICE`.

## İsim değişikliği (MASA → DivanAI)

Uygulama **MASA** adıyla yayınlanmadı; sürüm 1.25 ile birlikte adı **DivanAI** oldu.
Bu sürümden önce denemiş olanlar için tarayıcıdaki eski kayıtlar **kendiliğinden taşınır**:

| Eski kayıt | Yeni kayıt | Ne var içinde |
|---|---|---|
| `masa_settings_v1` | `divanai_settings_v1` | Bütün ayarlar, sağlayıcı, **API anahtarları** |
| `masa_session_v1` | `divanai_session_v1` | Yarım kalan konuşma, duraklatma kaydı |
| `masa_req_v1` | `divanai_req_v1` | Bugünkü istek sayacı |
| `masa_quota_v1` | `divanai_quota_v1` | Kota dolduğunda duraklatma |

Sayfayı bir kez açman yeterli: taşıma tek seferlik çalışır, ardından eski kayıt silinir.
**Hiçbir şeyi elle yapman gerekmez**; anahtarın ve ayarların yerinde kalır.
Daha önce indirdiğin `.json` ayar yedeği de açılmaya devam eder (dosya içindeki uygulama adı
`MASA` yazsa bile kabul edilir).

| Paylaş: bağlantı ve sohbet özeti | Telefonda paylaş penceresi |
|---|---|
| ![Paylaş](ekranlar/117-paylas.jpg) | ![Mobil](ekranlar/117-paylas-mobil.jpg) |

---

## Güvenlik

### Kısa cevap: sunucu yok, hesap yok, toplanan veri yok

DivanAI tek bir dosyadır. Çalışırken **hiçbir sunucuya bağlanmaz** — ne bizim, ne başkasının.
Konuşma senin tarayıcında oluşur, ekranda durur. Sayfayı kapatınca biter.

Tek istisna senin seçtiğin modeldir: yazdığın konu **doğrudan tarayıcından** o yüzden
seçtiğin servise (OpenRouter, Groq, OpenAI…) gider. Arada kimse yok, kopya çıkmaz.
Bunun anlamı şu: **yazdığın şeyi o servis görür.** Sır, kimlik numarası, hasta bilgisi
yazacaksan bunu bilerek yaz.

### Anahtarın nerede duruyor?

Tarayıcının kendi yerel deposunda (localStorage), **yalnız senin bilgisayarında**. Hiçbir yere
gönderilmez; sadece seçtiğin sağlayıcının adresine, `Authorization` başlığında gider.

Bu bir "kasa" değil, tarayıcının normal kayıt alanı: sayfayı yenilediğinde anahtar kaybolmasın diye
orada durur. Dışa aktarılan ayar yedeğine **yazılmaz**, paylaşılan bağlantıda görünmez. Ortak
kullanılan bir bilgisayardaysan **Ayarlar → Bağlantı → “Bu tarayıcıdan sil”** düğmesi anahtarı hem
depodan hem sandalyelerden siler.

Dikkat edilecek iki durum var:

| Durum | Ne yapmalı |
|---|---|
| Ortak kullanılan bilgisayar | DivanAI'yı açarken **Demo** modunu kullan; anahtar girme. Ya da işin bitince Ayarlar → anahtarı sil. |
| Tarayıcı eşitlemesi (Chrome/Firefox hesabı) | `localStorage` normalde eşitlenmez; yine de anahtarı tarayıcı hesabına bağlı bir profilde tutmak istemiyorsan ayrı profil kullan. |

Anahtar **hiçbir zaman** dışa aktarılan dosyaya yazılmaz. Ayarları yedeklerken anahtarlar
kasıtlı olarak dışarıda bırakılır — dosyayı paylaşsan bile anahtar içinde olmaz.

### Yayına verirken ne kontrol edildi

Bu sürüm yayına çıkmadan önce şunlar sınandı (34 otomatik güvenlik kontrolü):

- **Model cevabından kod çalıştırma (XSS).** Modelin cevabına gizlenmiş `<script>`, `onerror`,
  `onload`, `javascript:` bağlantısı ve `<iframe>` denendi. Hepsi **metin olarak** göründü,
  hiçbiri çalışmadı.
- **Zararlı ayar yedeği.** Başkasının gönderdiği bozuk bir `.json` yedeği ile sayfaya kod
  sokulmaya çalışıldı; çalışmadı.
- **Aynı cevap hafızada kalsa bile.** Konuşma tarayıcıda saklanıyor; sayfa yeniden açıldığında
  zararlı içerik yine çalışmadı.
- **Anahtar sızıntısı.** Canlı bir tur boyunca **bütün** ağ trafiği dinlendi: anahtar yalnız
  seçilen sağlayıcıya gitti, hiçbir adres satırında görünmedi, sayfada yazılı değil,
  dışa aktarılan dosyada yok. Ayrıca bir "tuzak sunucu" kuruldu: oraya **tek bir istek bile**
  gitmedi.
- **Dış kaynak.** Sayfada dışarıdan gelen script, stil, iframe, form veya reklam yok.

### İçerik güvenliği politikası (CSP)

Sayfaya bir **CSP** konuldu. Tek dosya olduğu için satır içi kod zorunlu; ama dışarıdan
**kod yüklenemez**: uzak script, iframe, eklenti (object), form gönderimi ve `<base>`
kaçırma kapalı. Yani yarın bir kaçış hatası bulunsa bile sayfaya dışarıdan kod çekilemez.
Politika sayfanın içinde `<meta>` ile veriliyor, çünkü GitHub Pages özel başlık göndermiyor.

Kol 117'de iki iz daha açıldı, ikisi de **yalnız kendi sitemize** (`'self'`): `worker-src`
(service worker dosyası) ve `manifest-src` (uygulama manifesti). Başka alan adından ne worker
ne manifest yüklenebilir; geri kalan her şey `'none'` olarak duruyor.

Ayrıca `Referrer-Policy: no-referrer` var: dış bir bağlantıya tıkladığında sayfa adresin
karşı tarafa sızmaz.

### Yerel sunucu (`server.py`)

İsteğe bağlı. Yalnız **127.0.0.1**'i (kendi bilgisayarın) dinler, ağdan erişilemez.
Klasör listesi kapalıdır, sürüm bilgisi gizlidir, bozuk adresler sunucuyu düşürmez.
Yayına alman gerekmez; GitHub Pages için gerekli değildir.

### Kullanıcı olarak senin tarafında kalan tek şey

- Konuyu yazarken neyin o servise gideceğini bil.
- Anahtarını kimseyle paylaşma; ekran görüntüsü alırken Ayarlar penceresini kapat.
- Şüpheli bir `.json` ayar yedeğini yalnız güvendiğin kişiden al.

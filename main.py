# -*- coding: utf-8 -*-
"""
Tefekkür-i Kâinat & Vahdet Bilinci | Contemplation of the Universe
Eksiksiz ve Güncellenmiş Streamlit Web Uygulaması
"""

import streamlit as st
import streamlit.components.v1 as components

# Sayfa Yapılandırması
st.set_page_config(
    page_title="Tefekkür-i Kâinat & Vahdet Bilinci | Contemplation of the Universe",
    page_icon="🌌",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Sağ Tık, Metin Seçimi ve Kopyalama Engelleyici (Anti-Copy JS & CSS)
ANTI_COPY_HTML = """
<script>
    document.addEventListener('contextmenu', event => event.preventDefault());
    document.addEventListener('keydown', function(e) {
        if ((e.ctrlKey || e.metaKey) && (e.key === 'c' || e.key === 'C' || e.key === 'u' || e.key === 'U' || e.key === 's' || e.key === 'S' || e.key === 'p' || e.key === 'P')) {
            e.preventDefault();
        }
    });
</script>
"""
components.html(ANTI_COPY_HTML, height=0, width=0)

# Göz Yormayan Ferah Tema (Krem / Bej Tonları) ve Sol Alta Dizilim CSS Stilleri
st.markdown("""
<style>
    /* Genel Arka Plan ve Yazı Rengi (Göz Yormayan Krem Tonu) */
    .stApp {
        background-color: #f9f6f0 !important;
        color: #2c3e50 !important;
    }
    
    /* Metin seçimi ve kopyalamayı devre dışı bırakma */
    body, .stApp, p, h1, h2, h3, h4, div, span, li {
        -webkit-user-select: none !important;
        -moz-user-select: none !important;
        -ms-user-select: none !important;
        user-select: none !important;
    }
    
    /* Ana Kart Tasarımı */
    .main-card {
        background-color: #ffffff;
        border: 1px solid #e3dec9;
        border-radius: 12px;
        padding: 28px;
        margin-bottom: 20px;
        color: #2c3e50;
        box-shadow: 0 4px 6px rgba(0,0,0,0.02);
    }
    
    /* Alıntı ve Kaynak Kutuları */
    .quote-box {
        background-color: #fdfbf7;
        border-left: 4px solid #b8860b;
        padding: 16px 20px;
        margin-bottom: 14px;
        border-radius: 0 8px 8px 0;
        color: #333333;
        border-top: 1px solid #f0e6d2;
        border-right: 1px solid #f0e6d2;
        border-bottom: 1px solid #f0e6d2;
    }
    
    /* Yasal Uyarı Kutusu */
    .legal-box {
        background-color: #f2eee3;
        border: 1px solid #d4c5a9;
        border-radius: 8px;
        padding: 14px;
        font-size: 0.85rem;
        color: #4a453b;
        margin-top: 25px;
    }

    /* Sol Tarafta Alt Alta Modül / Bölüm Başlığı */
    .module-header {
        font-weight: bold;
        color: #5c4033;
        margin-top: 15px;
        margin-bottom: 10px;
        font-size: 1.1rem;
        border-bottom: 2px solid #d4c5a9;
        padding-bottom: 5px;
    }
</style>
""", unsafe_allow_html=True)

# Çift Dilli Tam Kaynaklı Veritabanı (TR ve EN)
DATA = {
    "TR": {
        "app_title": "🌌 Tefekkür-i Kâinat & Vahdet Bilinci",
        "app_subtitle": "Kâinat Perdesinin Ardındaki Hakikati Okuma ve Net Kaynaklı Tefekkür Arşivi",
        "menu_title": "📚 Tefekkür Konuları",
        "section_title": "📌 Modüller ve Bölümler",
        "mod_reflection": "🧠 Derin Tefekkür & Bilimsel/Fennî Veriler",
        "mod_verses": "📖 Diyanet Mealli Ayetler (20 Kaynak)",
        "mod_hadiths": "🕌 Tahkik Edilmiş Hadisler (20 Kaynak)",
        "mod_sages": "🕊️ İslam Âlimleri & Eserleri (20 Kaynak)",
        "sleep_notice": (
            "💡 *Not:* Bu web uygulaması ücretsiz sunucularda barındırılmaktadır. "
            "Uzun süre işlem yapılmadığında uygulama uyku moduna geçebilir.\n\n"
            "💤 Eğer böyle bir ekranla karşılaşırsanız, ekranda beliren mavi renkli "
            "*'Yes, get this app back up!'* butonuna tıklayın ve 15-30 saniye bekleyin."
        ),
        "legal_title": "⚖️ YASAL UYARI, TELİF VE KULLANIM ŞARTLARI",
        "legal_text": (
            "© 2026 Tüm Hakları Saklıdır. Bu dijital eser; kâinatı ilahi hikmet penceresinden okumak, "
            "manevi farkındalık kazandırmak amacıyla bilgi paylaşımı için hazırlanmıştır. "
            "Ticari amaçla kullanılması, kopyalanması, çoğaltılması veya kaynak gösterilmeksizin alıntılanması yasaktır."
        ),
        "topics": {
            "1. Niyetin Simyası ve Teknolojiyle Hayır Yaymak": {
                "essay": """İnsanın elindeki her modern vasıta —yazılan bir kod satırı, kurulan bir web sitesi, havadaki elektromanyetik dalgalar— 
halis bir niyetle birleştiğinde ilahi bir hikmete ve kesintisiz bir iyilik köprüsüne dönüşür. 
Havaya karışan sinyallerin en ücra köşelere ulaşması gibi, niyetimiz de solunan her nefeste ve erişilen her ekranda 
hayrın, güzel bilginin ve hakikatin insanlara ulaşmasıdır.

Ortaya konulan hiçbir güzelliği nefsine mal etmemek; kendini yalnızca ilahi ikramın geçtiği aciz bir vesile olarak görmek, 
kulluğun en zarif edeplerindendir. Bir insana bir fayda ulaştığında övgüyü kendimize değil, mülkün gerçek sahibine yöneltmek 
ve o kişinin de Rabbine şükretmesini arzulamak, benliği aradan çıkarmanın (fena hâlinin) en canlı göstergesidir.

Fennî ve Bilimsel Yaklaşım: Elektromanyetik dalgaların ve fiber optik sinyallerin havadaki veya kablolardaki yayılım hızı 
fizik kanunlarına göre saniyede yaklaşık 300.000 kilometreye (ışık hızı) ulaşır. Bu durum, bilginin ve niyetin ulaştırıldığı 
mecraların ne denli geniş bir coğrafyaya anında nüfuz edebileceğinin fiziksel delilidir.""",
                "verses": [
                    "1. Kur'an-ı Kerim, Bakara Suresi, 261: 'Allah yolunda mallarını harcayanların durumu, her başağacında yüz danacı olmak üzere yedi başak veren bir tek tohumun durumu gibidir. Allah dilediğine kat kat verir. Allah lütfu geniş olandır, bilendir.' (Diyanet İşleri Başkanlığı Meali)",
                    "2. Kur'an-ı Kerim, İsrâ Suresi, 44: 'Yedi gök, yer ve bunlarda bulunanlar O'nu tespih ederler. O'nu övgü ile tespih etmeyen hiçbir şey yoktur. Ne var ki siz onların tespihlerini anlamazsınız. Şüphesiz O, halimdir, çok bağışlayandır.' (Diyanet İşleri Başkanlığı Meali)",
                    "3. Kur'an-ı Kerim, En'âm Suresi, 162: 'De ki: Şüphesiz benim namazım, ibadetlerim, hayatım ve ölümüm âlemlerin Rabbi olan Allah içindir.' (Diyanet İşleri Başkanlığı Meali)",
                    "4. Kur'an-ı Kerim, Bakara Suresi, 115: 'Doğu da batı da (tüm mülk) Allah'ındır. Nereye dönerseniz Allah'ın yüzü (kıblesi/tecellisi) oradadır. Şüphesiz Allah lütfu geniş olandır, bilendir.' (Diyanet İşleri Başkanlığı Meali)",
                    "5. Kur'an-ı Kerim, Ra'd Suresi, 15: 'Göklerde ve yerde bulunanlar ve onların gölgeleri sabah akşam isteyerek veya istemeyerek Allah'a secde ederler.' (Diyanet İşleri Başkanlığı Meali)",
                    "6. Kur'an-ı Kerim, Hicr Suresi, 29: 'Onu düzenleyip içine ruhumdan üflediğim zaman hemen ona secdeye kapanın.' (Diyanet İşleri Başkanlığı Meali)",
                    "7. Kur'an-ı Kerim, Hadîd Suresi, 4: 'O, gökleri ve yeri altı günde yaratan, sonra arşa istivâ edendir. Yere gireni, çıkanı, gökten ineni ve oraya çıkanı bilir. Nerede olursanız olun, O sizinle beraberdir. Allah yaptıklarınızı görmektedir.' (Diyanet İşleri Başkanlığı Meali)",
                    "8. Kur'an-ı Kerim, Kâf Suresi, 16: 'Andolsun, insanı biz yarattık ve nefsinin ona ne vesveseler verdiğini biliriz. Biz ona şah damarından daha yakınız.' (Diyanet İşleri Başkanlığı Meali)",
                    "9. Kur'an-ı Kerim, Zâriyât Suresi, 56: 'Ben cinleri ve insanları, ancak bana kulluk etsinler diye yarattım.' (Diyanet İşleri Başkanlığı Meali)",
                    "10. Kur'an-ı Kerim, İsrâ Suresi, 70: 'Andolsun ki biz âdemoğlunu şerefli kıldık; onları karada ve denizde taşıdık, kendilerine güzel rızıklar verdik ve onları yarattıklarımızın birçoğundan üstün kıldık.' (Diyanet İşleri Başkanlığı Meali)",
                    "11. Kur'an-ı Kerim, Mülk Suresi, 3: 'O, yedi göğü tabaka tabaka yaratandır. Rahmân'ın yaratmasında hiçbir uyumsuzluk göremezsin. Gözünü çevir de bak, bir bozukluk görebiliyor musun?' (Diyanet İşleri Başkanlığı Meali)",
                    "12. Kur'an-ı Kerim, Kamer Suresi, 49: 'Şüphesiz biz her şeyi bir ölçüye göre yarattık.' (Diyanet İşleri Başkanlığı Meali)",
                    "13. Kur'an-ı Kerim, Bakara Suresi, 216: 'Olur ki hoşunuza gitmeyen bir şey sizin için hayırlıdır ve olur ki sevdiğiniz şey de sizin için bir şerdir. Allah bilir, siz bilmezsiniz.' (Diyanet İşleri Başkanlığı Meali)",
                    "14. Kur'an-ı Kerim, Enbiyâ Suresi, 35: 'Her nefis ölümü tadacaktır. Sizi bir imtihan olarak hayır ile de şer ile de sınıyoruz. Ancak bize döndürüleceksiniz.' (Diyanet İşleri Başkanlığı Meali)",
                    "15. Kur'an-ı Kerim, İnşirah Suresi, 5-6: 'Elbette zorlukla beraber bir kolaylık vardır. Şüphesiz zorlukla beraber bir kolaylık vardır.' (Diyanet İşleri Başkanlığı Meali)",
                    "16. Kur'an-ı Kerim, Nahl Suresi, 18: 'Allah'ın nimetlerini saymaya kalksanız onları sayamazsınız. Şüphesiz Allah çok bağışlayandır, çok merhamet edendir.' (Diyanet İşleri Başkanlığı Meali)",
                    "17. Kur'an-ı Kerim, İbrahim Suresi, 7: 'Hani Rabbiniz şöyle duyurmuştu: Andolsun eğer şükrederseniz elbette size nimetimi artırırım, eğer nankörlük ederseniz hiç şüphesiz azabım şiddetlidir.' (Diyanet İşleri Başkanlığı Meali)",
                    "18. Kur'an-ı Kerim, Nûr Suresi, 35: 'Allah, göklerin ve yerin nurudur...' (Diyanet İşleri Başkanlığı Meali)",
                    "19. Kur'an-ı Kerim, Enfâl Suresi, 17: 'Onları siz öldürmediniz, bilakis onları Allah öldürdü. Attığın zaman da sen atmadın, bilakis Allah attı...' (Diyanet İşleri Başkanlığı Meali)",
                    "20. Kur'an-ı Kerim, Kehf Suresi, 110: 'De ki: Ben ancak sizin gibi bir insanım. Bana ilahınızın bir tek ilah olduğu vahyolunuyor. Kim Rabbine kavuşmayı umuyorsa salih amel işlesin ve Rabbine ibadette hiçbir şeyi ortak koşmasın.' (Diyanet İşleri Başkanlığı Meali)"
                ],
                "hadiths": [
                    "1. Kaynak: Sahih-i Buhari, Bedaü'l-Vahy, 1; Sahih-i Müslim, İmare, 155: 'Ameller ancak niyetlere göredir; herkese niyeti vardır.' — Bir işin dış görünüşü kadar ardındaki niyet de değer taşır; yazılan bir kod, paylaşılan bir bilgi veya yapılan bir hizmet halis bir niyetle birleştiğinde maddi sınırları aşan bir manevi karşılık ve bereket kazanır.",
                    "2. Kaynak: Sahih-i Müslim, Cenaiz, 14; Sünen-i Tirmizi, Hubut, 2: 'İnsan ölünce amelleri kesilir; ancak üç şey müstesnadır: Sadaka-i cariye, faydalanılan ilim ve kendisine dua eden salih evlat.' — İnsanların istifadesine sunulan sahih bilgi ve faydalı eserler, ardında kesintisiz devam eden bir hayır halkası ve dua kapısı açabilir.",
                    "3. Kaynak: Sahih-i Müslim, İmare, 133; Sünen-i Ebu Davud, Edeb, 115: 'Hayra vesile olan, hayrı yapan gibidir.' — Kendini öne çıkarmadan yalnızca bir imkân sunmak, bir yolu kolaylaştırmak ve bir iyiliğe vesile olmak, o iyiliğin bereketine ve sevabına ortak kılar.",
                    "4. Kaynak: Sahih-i Buhari, İman, 37; Sahih-i Müslim, İman, 1: Cibril Hadisi olarak bilinen rivayette ihsanın tarifi yapılmıştır: 'Allah'ı görüyormuşçasına O'na ibadet etmen; sen O'nu görmesen de O'nun seni gördüğünü bilmendir.' — Her işi en özenli, dürüst ve şuurlu biçimde yapmak ihsan bilincinin yansımasıdır.",
                    "5. Kaynak: Sahih-i Müslim, Zühd, 64: 'Müminin durumu ne gariptir; her işi onun için bir hayırdır. Bu durum müminden başkasına nasip olmaz. Ona bir genişlik ve sevinç gelse şükreder, bu onun için hayır olur; bir darlık ve zarar gelse sabreder, bu da onun için hayır olur.' — Teslimiyet ve rıza, her hâli manevi kazanca dönüştürür.",
                    "6. Kaynak: Sünen-i Tirmizi, Birr, 35: 'İnsanlara teşekkür etmeyen kimse Allah'a da şükretmemiştir.' — Emeği geçenlere, vesile olanlara ve iyilik ulaştıranlara karşı vefa göstermek, nimetin asıl sahibine yönelen şükrün ilk basamağıdır.",
                    "7. Kaynak: Sahih-i Müslim, Birr, 33: 'Şüphesiz Allah sizin suretlerinize ve mallarınıza bakmaz, ancak kalplerinize ve amellerinize bakar.' — Gösteriş ve dünyevi unvanların ötesinde, kalbin ihlası ve amelin samimiyeti belirleyicidir.",
                    "8. Kaynak: Sahih-i Müslim, İman, 71-72: 'İman etmedikçe cennete giremezsiniz, birbirinizi sevmedikçe de gerçek iman etmiş olamazsınız.' — Sevgi ve kardeşlik bağı, ortak hakikate yönelen kalplerin birbirine açtığı manevi bir penceredir.",
                    "9. Kaynak: Sünen-i Tirmizi, Birr, 36: 'Din kardeşine tebessüm etmen bir sadakadır.' — Küçük bir tebessüm ve yumuşak bir üslup, en sade ve en erişilebilir iyilik biçimlerinden biridir.",
                    "10. Kaynak: Sahih-i Buhari, Salat, 56; Sahih-i Müslim, Mesacid, 3: 'Yeryüzü bana mescit ve temiz kılınmıştır.' — Bütün yeryüzü ve içinde yaşanan mekânlar, kulluk ve tefekkür bilinciyle anlam kazanır.",
                    "11. Kaynak: Sahih-i Müslim, Salat, 215: 'Kulun Rabbine en yakın olduğu an secde hâlidir; bu nedenle duayı çoğaltın.' — Benliğin yere bırakıldığı secde, kul ile Yaratıcı arasındaki en samimi yakınlık makamıdır.",
                    "12. Kaynak: Sünen-i Tirmizi, Daavat, 9: 'Zikrin en efdali lâ ilâhe illallah, duânın en efdali elhamdülillah'tır.' — Tevhid ikrarı ile hamd ve şükür, dilin ve kalbin en kıymetli sermayesidir.",
                    "13. Kaynak: Sahih-i Buhari, Deavat, 66: 'Rabbini zikreden ile zikretmeyenin misali, diri ile ölü gibidir.' — Hakikatle bağ kurmak ve Yaratıcıyı anmak kalbe dirilik ve uyanıklık verir.",
                    "14. Kaynak: Sahih-i Müslim, İman, 147: 'Kalbinde zerre miktarı kibir olan kimse cennete giremez.' — Kibir, hakikati görmeyi perdeleyen en ince engellerden biridir; tevazu ise kalbi açar.",
                    "15. Kaynak: Sahih-i Müslim, Birr, 69: 'Kim Allah için tevazu gösterirse, Allah onu yüceltir.' — Nefsini küçültüp hakkı yücelten kul, ilahi katta değer ve vakarına kavuşur.",
                    "16. Kaynak: Sahih-i Buhari, İlim, 11; Müslim, Cihad, 4: 'Kolaylaştırınız, zorlaştırmayınız; müjdeleyiniz, nefret ettirmeyiniz.' — İlim ve hayır aktarımında üslup, anlaşılır kılmak ve ümit vermek esastır.",
                    "17. Kaynak: Taberani, Mu'cemü'l-Evsat, 6/309: 'İnsanların en hayırlısı, insanlara en çok faydalı olandır.' — Üretilen bilginin ve emeğin ölçüsü, başkalarının hayatına kattığı hayır ve kolaylıktır.",
                    "18. Kaynak: Sahih-i Buhari, Edeb, 34: 'Güzel söz de bir sadakadır.' — Kırıcı olmayan, yapıcı ve hikmetli her kelime gönüller arasında iyilik taşır.",
                    "19. Kaynak: Sahih-i Buhari, Rıkak, 3: 'Dünyada sanki bir garip veya yolcu gibi ol.' — Dünyaya aşırı bağlanmadan, geçici bir durakta emanetçi bilinciyle yürümek kalbi hafifletir.",
                    "20. Kaynak: Sünen-i Tirmizi, Daavat, 50: Sabah ve akşam zikirlerinin fazileti hakkında var olan sahih rivayetler. — Günün başlangıcını ve bitişini zikir ve sığınmayla çerçevelemek, iç dünyayı gün boyu koruma altına alır."
                ],
                "sages": [
                    "1. Kaynak: Bediüzzaman Said Nursî, Sözler (33. Söz - Ehadiyet Risalesi): Bir çiçeği yaratamayan güneşi de yaratamaz. — Kâinattaki en küçük bir zerrenin dahi tesadüf veya tabiatla izah edilemeyeceğini, her şeyin ancak her şeye kadir olan Vahid-i Ehad'in kudretiyle var olabileceğini ortaya koyar.",
                    "2. Kaynak: Mevlânâ Celâleddîn-i Rûmî, Mesnevi: Zıtlıkların hikmeti ve âlemin nizamı. — Gece-gündüz, soğuk-sıcak, darlık-genişlik gibi zıtlıkların kâinattaki hareketi, idraki ve tekâmülü mümkün kılan hikmetli bir düzen olduğunu anlatır.",
                    "3. Kaynak: İmam-ı Gazâlî, İhyâ: Beden mimarisi ve uyku mucizesi. — İnsan bedenindeki ince dengeleri ve uykunun yorgunluğu giderip bilinci tazeleyen hikmetini ilahi sanatın delilleri olarak işler.",
                    "4. Kaynak: Muhyiddin İbn Arabî, Füsûs: Şer ve kusur görünenlerin tablodaki renk uyumu. — İlk bakışta eksik veya sert görünen unsurların, bütünün büyük tablosunda denge ve anlam tamamladığını vurgular.",
                    "5. Kaynak: İbrahim Hakkı Erzurumî, Marifetname: Zerrattan küreye hikmetler. — En küçük parçacıktan gök cisimlerine kadar uzanan geniş yaratılış zincirindeki ilahi düzeni ve insanın bu bütündeki yerini açıklar.",
                    "6. Kaynak: Şah-ı Nakşibend, Nasihatler: İmtihanda rıza göstermek. — Karşılaşılan hadiseler karşısında isyan yerine teslimiyet ve rıza ile durmanın kalbi sükûnete ulaştıracağını öğretir.",
                    "7. Kaynak: Yunus Emre, Divan: Kudretin tecellisi. — Varlıktaki her güzelliğin ve hareketin, görünmeyen Mutlak Kudretin bir yansıması ve işareti olduğunu sade ve derin bir dille dile getirir.",
                    "8. Kaynak: Abdülkâdir Geylânî, Gunyetü't-Talibîn: Sıkıntıların hikmeti. — Sıkıntı ve imtihanların kulun gafletten uyanması, sabrının olgunlaşması ve Rabbine yönelmesi için bir vesile olduğunu bildirir.",
                    "9. Kaynak: İmam-ı Rabbânî, Mektûbât: Memur olan varlıklar. — Kâinattaki hiçbir varlığın kendi başına ve başıboş olmadığını, her birinin ilahi emirle vazife gören memurlar hükmünde bulunduğunu açıklar.",
                    "10. Kaynak: Sadreddin Konevî, Miftâhü'l-Gayb: Ehadiyet mührünün sırrı. — Çokluk perdesi arkasında birliğin nasıl okunabileceğini ve varlık mertebelerindeki hikmetli irtibatı inceler.",
                    "11. Kaynak: Cüneyd-i Bağdâdî, Risaleler: Verilmeyen nimetin hikmeti. — İstenen bir şeyin verilmemesinin ardında da kulun bilmediği bir hikmet ve koruma bulunabileceğini hatırlatır.",
                    "12. Kaynak: Hacı Bayrâm-ı Velî, Menakıb: İnsan meyvesi. — Kâinat ağacının en olgun ve bilinçli meyvesinin marifet ve kullukla kemale eren insan olduğunu vurgular.",
                    "13. Kaynak: Beyazıd-i Bistâmî: İmtihandaki gizli lütuflar. — Zahirde ağır görünen hâllerin içinde dahi ilahi inayetin ve terbiyenin gizli bulunduğunu ifade eder.",
                    "14. Kaynak: Niyâzî-i Mısrî, Divan: Üç boyutlu suret perdesi. — Görünen maddi şekillerin arkasındaki manaya ve hakikate göz açmanın gerekliliğini işler.",
                    "15. Kaynak: Eşrefoğlu Rûmî, Müzekki'n-Nüfûs: Gafletten uyanış. — Nefsin aldatıcı heveslerinden sıyrılıp kalbi arındırmanın ve hakikate uyanmanın yollarını gösterir.",
                    "16. Kaynak: Aziz Mahmud Hüdâyî, Vâkıfat: Vazifesini yapan zerrat. — Kâinattaki en küçük zerrelerin bile kendilerine verilen vazifeyi kusursuzca yerine getirerek Rabbine boyun eğdiğini anlatır.",
                    "17. Kaynak: Ferîdüddîn Attâr, Tezkiretü'l-Evliya: Karıncanın azmi. — Küçük bir canlının bile gayesine ulaşmadaki sebatı ve kararlılığı üzerinden manevi gayreti örnekler.",
                    "18. Kaynak: Hasan-ı Basrî, Zühd: Ömür sermayesi. — Geçen her günün ömür sermayesinden eksilen bir parça olduğunu hatırlatarak zamanı hikmetle değerlendirmeye çağırır.",
                    "19. Kaynak: Sehl et-Tüsterî, Tefsir: Nimetin hakiki şükrü. — Gerçek şükrün, nimetin kaynağını bilmek ve o nimeti Yaratıcının razı olacağı hayırlı yollarda kullanmak olduğunu belirtir.",
                    "20. Kaynak: Ken'ân Rifâî, Sohbetler: Çile ve terakki. — Sabırla karşılanan zahmetlerin insanı olgunlaştırıp manevi bir olgunluğa (terakkiye) taşıdığını anlatır."
                ]
            },
            "2. Kâinatla Birlikte Zikir, Salavat ve Kesintisiz Secde": {
                "essay": """Secde, yalnızca alnın belli vakitlerde toprağa değmesiyle sınırlı bir şekil ibadeti değildir; o, kulun kendi benliğini 
yok sayıp (fena bulup) kâinatın kesintisiz ibadet halkasına bilinçli bir zerre olarak katılmasıdır. 
Yürürken ayaklarımızın toprağa, tenimizin ve bütün vücudumuzun havaya temas etmesi; suya girdiğimizde suyun 
bütün varlığımızı kuşatması, elementlerin o muazzam secdesine bizim de dâhil oluşumuzdur.

Kâinattaki taş, toprak, yıldızlar ve tüm mahlukat kendi yaratılış kanunları gereği istemli veya isteksiz 
gölgeleriyle birlikte her an secde hâlindedir. İnsan ise aklı ve iradesiyle bu büyük koroya katıldığında zikri derinleşir.

Fennî ve Bilimsel Yaklaşım: Biyofizikte ve termodinamikte insan vücudunun sürekli olarak atmosferik basınç, 
yer çekimi (9.81 m/s²) ve sıvı hidrodinamik kuvvetler altında bulunduğu kanıtlanmıştır. Cildin hava ile teması 
ve vücudun su oranı (ortalama %60-70), fiziksel olarak kâinattaki elementer ekosistemle tam bir fiziksel temas ve uyum içindedir.""",
                "verses": [
                    "1. Kur'an-ı Kerim, Ra'd Suresi, 15: 'Göklerde ve yerde kim varsa, ister istemez kendileri de gölgeleri de sabah akşam Allah'a secde ederler.' (Diyanet İşleri Başkanlığı Meali)",
                    "2. Kur'an-ı Kerim, Hac Suresi, 18: 'Görmedin mi ki göklerde ve yerde olanlar, güneş, ay, yıldızlar, dağlar, ağaçlar, hayvanlar ve insanlardan birçoğu Allah'a secde etmektedir...' (Diyanet İşleri Başkanlığı Meali)",
                    "3. Kur'an-ı Kerim, Nahl Suresi, 49: 'Göklerde ve yerde bulunan canlılar ve bütün melekler, kibirlenmeden Allah'a secde ederler.' (Diyanet İşleri Başkanlığı Meali)",
                    "4. Kur'an-ı Kerim, Ahzâb Suresi, 56: 'Şüphesiz Allah ve melekleri Peygamber'e salât ederler. Ey iman edenler! Siz de ona salât edin ve tam bir teslimiyetle selam verin.' (Diyanet İşleri Başkanlığı Meali)",
                    "5. Kur'an-ı Kerim, İsrâ Suresi, 44: 'Yedi gök, yer ve bunlarda bulunanlar O'nu tespih ederler...' (Diyanet İşleri Başkanlığı Meali)",
                    "6. Kur'an-ı Kerim, Nûr Suresi, 41: 'Göklerde ve yerde olanların, kanatlarını açıp uçan kuşların Allah'ı tespih ettiğini görmedin mi? Her biri kendi duasını ve tespihini kesin olarak bilmiştir...' (Diyanet İşleri Başkanlığı Meali)",
                    "7. Kur'an-ı Kerim, Enbiyâ Suresi, 79: '...Dağları ve kuşları, Davut ile birlikte tespih etmeleri için boyun eğdirmiştik...' (Diyanet İşleri Başkanlığı Meali)",
                    "8. Kur'an-ı Kerim, Haşr Suresi, 24: 'O, yaratan, yoktan var eden, şekil veren Allah'tır. En güzel isimler O'nundur. Göklerde ve yerde ne varsa O'nu tespih eder. O, mutlak güç sahibidir, hüküm ve hikmet sahibidir.' (Diyanet İşleri Başkanlığı Meali)",
                    "9. Kur'an-ı Kerim, Cum'a Suresi, 1: 'Göklerde ve yerde ne varsa, mülkün sahibi, eksiklikten münezzeh, aziz ve hakim olan Allah'ı tespih eder.' (Diyanet İşleri Başkanlığı Meali)",
                    "10. Kur'an-ı Kerim, Tegâbün Suresi, 1: 'Göklerde ve yerde ne varsa Allah'ı tespih eder. Mülk O'nundur, hamd O'na mahsustur. O her şeye kadirdir.' (Diyanet İşleri Başkanlığı Meali)",
                    "11. Kur'an-ı Kerim, Alak Suresi, 19: 'Sakın ona uyma! Secde et ve (Rabbine) yaklaş.' (Diyanet İşleri Başkanlığı Meali)",
                    "12. Kur'an-ı Kerim, A'râf Suresi, 206: 'Şüphesiz Rabbinin katındakiler O'na ibadet etmekten kibirlenmezler, O'nu tespih ederler ve yalnız O'na secde ederler.' (Diyanet İşleri Başkanlığı Meali)",
                    "13. Kur'an-ı Kerim, Secde Suresi, 15: 'Bizim ayetlerimize ancak kendilerine hatırlatıldığı zaman secdeye kapanan, büyüklük taslamadan rablerini hamd ile tespih edenler inanır.' (Diyanet İşleri Başkanlığı Meali)",
                    "14. Kur'an-ı Kerim, Furkân Suresi, 64: 'Onlar ki, gecelerini Rablerine secde ederek ve kıyam durarak geçirirler.' (Diyanet İşleri Başkanlığı Meali)",
                    "15. Kur'an-ı Kerim, Fetih Suresi, 29: '...Onların nişanları yüzlerindeki secde izidir...' (Diyanet İşleri Başkanlığı Meali)",
                    "16. Kur'an-ı Kerim, Bakara Suresi, 152: 'Öyleyse beni anın ki ben de sizi anayım. Bana şükredin, sakın nankörlük etmeyin.' (Diyanet İşleri Başkanlığı Meali)",
                    "17. Kur'an-ı Kerim, Ahzâb Suresi, 41-42: 'Ey iman edenler! Allah'ı çokça zikredin. Ve O'nu sabah akşam tespih edin.' (Diyanet İşleri Başkanlığı Meali)",
                    "18. Kur'an-ı Kerim, Ra'd Suresi, 28: 'Bunlar, iman edenler ve gönülleri Allah'ın zikriyle sükûnota erenlerdir. Bilesiniz ki kalpler ancak Allah'ı anmakla huzur bulur.' (Diyanet İşleri Başkanlığı Meali)",
                    "19. Kur'an-ı Kerim, Tâhâ Suresi, 14: 'Şüphesiz ben Allah'ım. Benden başka ilah yoktur. Bana ibadet et ve beni anmak için namazı kıl.' (Diyanet İşleri Başkanlığı Meali)",
                    "20. Kur'an-ı Kerim, Ankebût Suresi, 45: '...Şüphesiz Allah'ı anmak (zikir) en büyük ibadettir...' (Diyanet İşleri Başkanlığı Meali)"
                ],
                "hadiths": [
                    "1. Kaynak: Sahih-i Müslim, Salat, 215: 'Kulun Rabbine en yakın olduğu an secde hâlidir.' — Secde, kulun en yüksek makamına başını ve benliğini koyarak ilahi yakınlığa eriştiği özel bir hâldir.",
                    "2. Kaynak: Sahih-i Müslim, Salat, 70: 'Kim bana bir defa salavat getirirse, Allah ona on rahmet ihsan eder.' — Salavat, Peygamber Efendimize (s.a.v.) sevgi ve saygının yanı sıra kulun kendi üzerine inen rahmet ve bereket kapısıdır.",
                    "3. Kaynak: Sahih-i Buhari, Salat, 56: 'Yeryüzü bana mescit ve temiz kılındı.' — Tabiatın ve toprağın kirlilikten arındırılmış bir kulluk ve secde mekânı olarak görülmesini ifade eder.",
                    "4. Kaynak: Sahih-i Müslim, Salat, 225: 'Allah için yapılan her secde bir derece yükseltir ve günahı siler.' — Her secde, manevi mertebede yükseliş ve kalbi ağırlaştıran kusurlardan arınmadır.",
                    "5. Kaynak: Sahih-i Müslim, Salat, 226: Hz. Rabia b. Ka'b'a Peygamberimizin secde konusunda tavsiyesi. — Cennette beraberlik dileğine karşılık Peygamberimizin 'Öyleyse çokça secde ederek bana yardımcı ol' buyurması, secdenin kulluktaki merkezi yerini gösterir.",
                    "6. Kaynak: Sünen-i Tirmizi, Daavat, 4: 'Dilin sürekli Allah'ın zikriyle ıslak kalsın.' — Zikrin günün belli anlarına sıkışmayıp hayatın akışı içinde süreklilik kazanmasını öğütler.",
                    "7. Kaynak: Sahih-i Buhari, Deavat, 65: 'Mizanda ağır gelen iki hafif kelime...' — 'Sübhanallahi ve bihamdihi, sübhanallahil-azim' tesbihlerinin telaffuzda hafif, manevi tartıda ise son derece ağır ve değerli olduğunu bildirir.",
                    "8. Kaynak: Sahih-i Müslim, Zikr, 38: Allah'ı zikreden meclisleri meleklerin kuşatması. — Zikir ve hakikat sohbetlerinin bulunduğu ortamların rahmet ve meleklerin kuşatmasıyla bereketlendiğini anlatır.",
                    "9. Kaynak: Sünen-i Ebu Davud, Salat, 207: 'Cuma günü bana salavatı artırın.' — Cuma gününün manevi atmosferinde salavatı çoğaltmanın özel bir karşılığı bulunduğunu vurgular.",
                    "10. Kaynak: Sünen-i Tirmizi, Vitir, 21: Kıyamet günü en yakın olanlar. — Güzel ahlakı ve Peygamberimize bağlılığı ile öne çıkanların manevi yakınlığa nail olacağını ifade eder.",
                    "11. Kaynak: Ahmed bin Hanbel, Müsned: Katılımlı tespih rivayetleri. — Varlıkların ve inananların tesbihle buluşmasının uyumlu ve bereketli yönüne işaret eder.",
                    "12. Kaynak: Sünen-i Ebu Davud, Edeb, 97: Abdestli uyumanın fazileti. — Gece istirahatine dahi taharet ve zikir bilinciyle girmenin ruhu koruduğunu gösterir.",
                    "13. Kaynak: Sahih-i Müslim, Zühd, 67: Yeryüzünde tevazu ile yürümek. — Toprağa basarken vakar ve alçakgönüllülükle yürümek, kâinatın ahengine uyum sağlamanın bir gereğidir.",
                    "14. Kaynak: Sünen-i Tirmizi, Daavat, 129: Tespih ve tekbirin sevabı. — Allah'ı noksan sıfatlardan tenzih etmenin ve büyüklüğünü dile getirmenin kalbe verdiği kuvveti anlatır.",
                    "15. Kaynak: Sünen-i Ebu Davud, Edeb, 105: Tabiat olayları karşısında dua. — Rüzgâr, yağmur ve gök gürültüsü gibi tabiat hadiseleri karşısında ilahi kudrete sığınma ve şükür bilincini öğretir.",
                    "16. Kaynak: Sünen-i İbn Mace, Taharet, 48: Suyu tasarruflu kullanmak ve çevre. — Akan bir nehrin kenarında dahi olsa suyu israf etmemeyi emrederek tabiat ve nimetlere karşı ölçülü olmayı öğretir.",
                    "17. Kaynak: Sahih-i Buhari, Edeb, 75: Secde azaplarının nefsaniyeti kırması. — Secde hâlinin nefsin gurur ve benlik iddialarını eritip kalbi yumuşattığını ortaya koyar.",
                    "18. Kaynak: Sahih-i Müslim, Müsafirin, 166: Gece ibadeti ve secde. — Gecenin sessizliğinde yapılan kıyam ve secdelerin kalpte derin bir nur ve huzur oluşturduğunu bildirir.",
                    "19. Kaynak: Beyhakî, Şuabü'l-İman: Müminin bakışı ve tefekkürü. — İbret ve tefekkürle atılan bakışın kulluk ve marifet yolunu açtığını ifade eder.",
                    "20. Kaynak: Taberani, Mu'cemü'l-Kebir: Tefekkürün ibadet değeri. — Yaratılmışlar üzerinde derin düşünmenin kalbi uyanık tutan kıymetli bir manevi amel olduğunu gösterir."
                ],
                "sages": [
                    "1. Kaynak: Mevlânâ Celâleddîn-i Rûmî, Fihi Ma Fih: Kümbet altında dönen her zerre aşkla döner. — Gök kubbesi altındaki her atomun ve varlığın kendi yörüngesinde ve vazifesinde ilahi bir cezbe ve ahenkle hareket ettiğini anlatır.",
                    "2. Kaynak: Muhyiddin İbn Arabî, Futuhat-ı Mekkiyye: Kâinat secdegâhtır. — Bütün kâinatın Yaratıcının huzurunda boyun eğen ve secde eden bir kulluk alanı olduğunu dile getirir.",
                    "3. Kaynak: Yunus Emre, Risaletü'n-Nushiyye: Dağlar ve taşlar ile zikir. — Dağların, suların ve tüm tabiatın kendi diliyle Hakkı andığını ve insanın da bu zikre ortak olması gerektiğini vurgular.",
                    "4. Kaynak: İmam-ı Gazâlî, Kimyâ-yı Saâdet: Hakiki secde kalbin teslimiyetidir. — Bedenin yere kapanmasıyla birlikte kalbin de kibir ve masivadan sıyrılıp tamamen Hakk'a teslim olmasını esas alır.",
                    "5. Kaynak: İbrahim Hakkı Erzurumî, Marifetname: Kâinat orkestrası ve şef irfanı. — Kâinattaki her sesin ve hareketin tek bir Kudretin idaresinde uyumlu bir bütün oluşturduğunu anlatır.",
                    "6. Kaynak: Abdülkâdir Geylânî, Cilâü'l-Hâtır: Ruhun daima secdede kalması. — Beden meşguliyetler içinde olsa dahi ruhun ve kalbin yönelişinin daima Yaratıcıya dönük kalmasını öğütler.",
                    "7. Kaynak: Cüneyd-i Bağdâdî, Lemaat: Zikirde fena bulmak. — Zikir esnasında kulun kendi varlığını ve iddiasını unutup yalnızca Zikredilen'in büyüklüğünde erimesini ifade eder.",
                    "8. Kaynak: Şems-i Tebrîzî, Makalat: Gölgeyi aradan çekmek. — Geçici benlik ve gölge varlıkların ötesine geçip asıl hakikate yönelmenin önemini vurgular.",
                    "9. Kaynak: Bediüzzaman Said Nursî, Mektubat (20. Mektup): Zerrattan yıldızlara tespihat. — En küçük zerreden en büyük yıldıza kadar her varlığın kendi lisanıyla Allah'ın isimlerini tespih ettiğini delilleriyle açıklar.",
                    "10. Kaynak: Niyâzî-i Mısrî, Mektubat: İrfan ve zikir. — Zikrin kuru bir tekrardan ibaret kalmayıp kalpte irfan ve farkındalık uyandırması gerektiğini belirtir.",
                    "11. Kaynak: Hacı Bektaş-ı Velî, Makalat: Cemal ve kemal sırrı. — Varlıktaki güzellik ve olgunluğun ardındaki ilahi sırrı ve edep yolunu gösterir.",
                    "12. Kaynak: Aziz Mahmud Hüdâyî, Nefâisü'l-Mecâlis: Hava zermelerinin zikri. — Solunan havadaki ve mekândaki en ince zerrelerin dahi kendi yaratılış kanunlarıyla Hakk'ı zikrettiğini anlatır.",
                    "13. Kaynak: Beyazıd-i Bistâmî, Risaleler: İbadette fena. — Kulun kendi ibadetini ve halini bir övünç vesilesi değil, ilahi lütfun bir tecellisi olarak görmesini ifade eder.",
                    "14. Kaynak: İmam-ı Rabbânî, Mektûbât: Sünnet ve salavatın nuru. — Peygamber sünnetine ittiba ve salavatın kalbi aydınlatan, kulluğu sahih ve nurlu kılan bir kaynak olduğunu açıklar.",
                    "15. Kaynak: Eşrefoğlu Rûmî, Tarîkatnâme: Tabiatın tespihine ortak olmak. — Kâinattaki canlı-cansız varlıkların zikrine bilinçli bir şuurla katılmanın manevi değerini işler.",
                    "16. Kaynak: Hallâc-ı Mansûr, Kitâbü't-Tavâsîn: Tevhid ve şuur. — Çokluk içinde birliği idrak etme ve hakikat şuuruna erme arayışını derin sembollerle dile getirir.",
                    "17. Kaynak: Sadreddin Konevî, İ‘câzü’l-Beyân: Gölgelerin secdesi. — Sabah akşam uzayıp kısalan gölgelerin dahi ilahi kudrete boyun eğen birer işaret olduğunu inceler.",
                    "18. Kaynak: Ahmed Yesevî, Divan-ı Hikmet: Seher vakti zikri. — Seher vaktinin dinginliğinde yapılan zikir ve niyazın ruhu arındıran derin tesirini anlatır.",
                    "19. Kaynak: Ferîdüddîn Attâr, Mantıku't-Tayr: Varlığın tesbihi. — Kuşların ve tüm varlıkların kendi dilleriyle hakikate doğru yürüdükleri sembolik bir tefekkür tablosu sunar.",
                    "20. Kaynak: Ken'ân Rifâî, Sohbetler: Namazın ruhunu kâinata yaymak. — Namaz ve secdedeki huşunun yalnızca belli dakikalara hapsedilmeyip tüm hayata ve kâinata yayılması gerektiğini vurgular."
                ]
            },
            "3. Ehadiyet Mührü, Karınca ile Güneş ve Zıtlıkların Hikmeti": {
                "essay": """Kâinat, ardındaki Mutlak Kudreti gösteren üç boyutlu muazzam bir perdedir. Bu perdede en küçük zerreden en büyük galaksiye 
kadar her şeyde aynı Sanatkar'ın "Ehadiyet mührü" vardır. Güneş o devasa kütlesi ve yakıcı enerjisine rağmen küçücük bir 
karıncanın sahip olduğu sanat inceliğine ve hayat mucizesine sahip değildir; karınca da güneşin kâinatı ısıtma ve 
aydınlatma vazifesini yapamaz. Her bir varlık, kendisine verilen emir ve ölçü dairesinde kusursuz bir görev icra eder.

İnsan ise bütün bu yaratılanların içinde mükerrem kılınmış yeryüzü halifesidir. Uyurken dahi vücudundaki trilyonlarca hücre, 
organlar ve sistemler ona hizmet etmeye devam eder. Allah nimetini hem insana hem de bütün yaratılanlara adaletle 
paylaştırmıştır; sadece birisine verseydi kâinatın dengesi bozulurdu. Kâinatta zorlukların, kusurların ve zıtlıkların 
yaratılmış olması da insanın tekâmülü ve terakkisi içindir; zıtlıklar olmasaydı iyiliğin değeri bilinmez ve insan ruhu 
olgunlaşamazdı.

Fennî ve Bilimsel Yaklaşım: Biyolojide karıncanın (Formicidae) kendi ağırlığının 20 ila 50 katı kadar yükü taşıyabilmesi, 
ekosistemdeki kusursuz mekanik ve hidrolik tasarıma delildir. Güneş ise devasa bir füzyon reaktörüdür ancak bilinç ve hayat 
mucizesinden mahrumdur. Hücre fizyolojisinde uyku esnasında dahi otonom sinir sistemi ve bazal metabolizma çalışarak 
insanı hayatta tutar; bu durum tıp biliminde homeostazi ve organ sistemlerinin muazzam işbirliği ile açıklanır.""",
                "verses": [
                    "1. Kur'an-ı Kerim, İhlâs Suresi, 1-2: 'De ki: O, Allah birdir. Allah sameddir (her şey O'na muhtaçtır, O hiçbir şeye muhtaç değildir).' (Diyanet İşleri Başkanlığı Meali)",
                    "2. Kur'an-ı Kerim, Neml Suresi, 18: 'Nihayet karınca vadisine geldikleri zaman, bir karınca şöyle dedi: 'Ey karıncalar! Yuvalarınıza girin, Süleyman ve ordusu farkına varmadan sizi ezmesinler.'' (Diyanet İşleri Başkanlığı Meali)",
                    "3. Kur'an-ı Kerim, Yâsîn Suresi, 38-40: 'Güneş de müstakarın (zamanı ve yeri) durup akıp gitmektedir. Bu, aziz ve alim olan Allah'ın takdiridir. Aya da birtakım menziller (evreler) tayin ettik... Ne güneş aya yetişebilir ne de gece gündüzü geçebilir. Her biri bir yörüngede yüzmektedir.' (Diyanet İşleri Başkanlığı Meali)",
                    "4. Kur'an-ı Kerim, Bakara Suresi, 30: 'Hani Rabbin meleklere, 'Ben yeryüzünde bir halife yaratacağım' demişti...' (Diyanet İşleri Başkanlığı Meali)",
                    "5. Kur'an-ı Kerim, Tîn Suresi, 4: 'Andolsun biz insanı en güzel biçimde (ahsen-i takvîm) yarattık.' (Diyanet İşleri Başkanlığı Meali)",
                    "6. Kur'an-ı Kerim, Câsiye Suresi, 13: 'O, göklerde ve yerde ne varsa hepsini, kendi katından (bir lütuf olarak) sizin hizmetinize verdi. Şüphesiz bunda düşünen bir toplum için ibretler vardır.' (Diyanet İşleri Başkanlığı Meali)",
                    "7. Kur'an-ı Kerim, Mülk Suresi, 2: 'O, hanginizin daha güzel amel edeceğini sınamak için ölümü ve hayatı yaratandır. O, mutlak güç sahibidir, çok bağışlayandır.' (Diyanet İşleri Başkanlığı Meali)",
                    "8. Kur'an-ı Kerim, Enbiyâ Suresi, 35: 'Her nefis ölümü tadacaktır. Sizi bir imtihan olarak hayır ile de şer ile de sınıyoruz...' (Diyanet İşleri Başkanlığı Meali)",
                    "9. Kur'an-ı Kerim, Şems Suresi, 7-10: 'Nefse ve ona şekil verene, sonra da ona iyilik ve kötülük kabiliyetini ilham edene yemin olsun ki, nefsini arındıran kurtuluşa ermiştir.' (Diyanet İşleri Başkanlığı Meali)",
                    "10. Kur'an-ı Kerim, Rahmân Suresi, 7-9: 'Göğü yükseltti ve mizanı (dengeyi) koydu. Sakın tartıda taşkınlık etmeyin. Tartıyı adaletle yapın, teraziyi eksiltmeyin.' (Diyanet İşleri Başkanlığı Meali)",
                    "11. Kur'an-ı Kerim, Furkân Suresi, 2: 'O, göklerin ve yerin mülkü kendisine ait olan, çocuk edinmeyen, mülkünde hiçbir ortağı bulunmayan, her şeyi yaratan ve ona bir düzen veren, bir ölçü tayin eden Allah'tır.' (Diyanet İşleri Başkanlığı Meali)",
                    "12. Kur'an-ı Kerim, Zümer Suresi, 9: '...De ki: Hiç bilenlerle bilmeyenler bir olur mu? Ancak akıl sahipleri öğüt alırlar.' (Diyanet İşleri Başkanlığı Meali)",
                    "13. Kur'an-ı Kerim, Bakara Suresi, 164: 'Şüphesiz göklerin ve yerin yaratılışında, gece ile gündüzün birbiri ardınca gelmesinde, insanlara fayda veren şeylerle denizde yüzen gemilerde, Allah'ın gökten indirip de yeri ölümünden sonra hayata kavuşturduğu suda, yeryüzünde yaydığı her türlü canlıda, rüzgârları ve gökle yer arasında emre amade bekleyen bulutları döndürmesinde düşünen bir toplum için elbette deliller vardır.' (Diyanet İşleri Başkanlığı Meali)",
                    "14. Kur'an-ı Kerim, Rûm Suresi, 22: 'Göklerin ve yerin yaratılması, dillerinizin ve renklerinizin farklı olması da O'nun delillerindendir. Şüphesiz bunda bilenler için ibretler vardır.' (Diyanet İşleri Başkanlığı Meali)",
                    "15. Kur'an-ı Kerim, Hûd Suresi, 6: 'Yeryüzünde hiçbir canlı yoktur ki, rızkı Allah'a ait olmasın. O, onların karar kıldıkları yeri de, emanet bırakıldıkları yeri de bilir. Bunların hepsi apaçık bir kitaptadır.' (Diyanet İşleri Başkanlığı Meali)",
                    "16. Kur'an-ı Kerim, En'âm Suresi, 38: 'Yeryüzünde yürüyen hiçbir hayvan ve kanatlarıyla uçan hiçbir kuş yoktur ki, sizin gibi birer ümmet olmasınlar...' (Diyanet İşleri Başkanlığı Meali)",
                    "17. Kur'an-ı Kerim, Secde Suresi, 7: 'O, yarattığı her şeyi güzel yapan ve insanı çamurdan yaratmaya başlayandır.' (Diyanet İşleri Başkanlığı Meali)",
                    "18. Kur'an-ı Kerim, Zâriyât Suresi, 20-21: 'Yeryüzünde kesin olarak inananlar için ayetler vardır. Kendi nefislerinizde de öyle. Hâlâ göremeyecek misiniz?' (Diyanet İşleri Başkanlığı Meali)",
                    "19. Kur'an-ı Kerim, Gâşiye Suresi, 17-20: 'Bakmıyorlar mı o develere, nasıl yaratılmıştır! Göğe, nasıl yükseltilmiştir! Dağlara, nasıl dikilmiştir! Yere, nasıl yayılmıştır!' (Diyanet İşleri Başkanlığı Meali)",
                    "20. Kur'an-ı Kerim, Âl-i İmrân Suresi, 191: 'Onlar ayaktayken, otururken ve yanları üzerindeyken Allah'ı anarlar; göklerin ve yerin yaratılışı üzerinde tefekkür ederler...' (Diyanet İşleri Başkanlığı Meali)"
                ],
                "hadiths": [
                    "1. Kaynak: Sahih-i Müslim, Selam, 47: 'Şüphesiz Allah güzeldir, güzelliği sever.' — Kâinattaki sanatkârane düzen, ölçü ve estetik; güzeli yaratan ve seven Mutlak Cemal sahibinin varlığına işaret eder.",
                    "2. Kaynak: Sahih-i Buhari, Marda, 1: Müminin her türlü zorluktan ders çıkararak terakki etmesi. — Karşılaşılan imtihan ve zorluklar, bilinçli bir tefekkür ve sabırla birleştiğinde manevi olgunluk ve ilerleme vesilesi olur.",
                    "3. Kaynak: Sünen-i Tirmizi, İlim, 13: 'İlim öğrenmek her Müslümana farzdır.' — Hem dini hem de kâinatın kanunlarını anlamaya yönelik ilim, insanın yaratılış gayesini idrak etmesinin temelidir.",
                    "4. Kaynak: Ahmed bin Hanbel, Müsned: 'Nefsini bilen Rabbini bilir' hikmetli yaklaşımı. — Kendi bedenindeki ince nizamı, acziyeti ve ihsanı tefekkür eden insan, bunları yaratan ve idare eden Rabbini daha derin tanır.",
                    "5. Kaynak: Sahih-i Buhari, Bedu'l-Halk, 15: Karıncalara merhamet ve canlı hakları. — Küçük bir karıncanın dahi incitilmemesini öğütleyen bu yaklaşım, en küçük canlıdaki hayat ve sanata hürmeti gösterir.",
                    "6. Kaynak: Sahih-i Tirmizi, Zühd, 57: İmtihanların derecesine göre olması. — Herkesin tahammülü ve manevi makamıyla orantılı olarak sınanması, ilahi adalet ve hikmetin bir tecellisidir.",
                    "7. Kaynak: Sahih-i Buhari, Rıkak, 1: 'İki nimet vardır ki insanların çoğu o hususta aldanmıştır: Sağlık ve boş vakit.' — Eldeki sıhhat ve zaman sermayesini tefekkür, ilim ve hayır yolunda değerlendirmenin önemi vurgulanır.",
                    "8. Kaynak: Sünen-i İbn Mace, Zühd, 15: Uyku ve uyanıklıkta azaların şükrü. — Görme, işitme, hareket etme ve dinlenme gibi her bir uzvun nimetinin farkında olup şükrünü yerine getirmek gerekir.",
                    "9. Kaynak: Taberani, Mu'cemü'l-Kebir: Tefekkürün ehemmiyeti. — Kâinat ve nefis üzerinde yapılan derin tefekkür, gaflet perdesini kaldırıp hakikate ulaştıran temel bir ibadettir.",
                    "10. Kaynak: Sahih-i Müslim, Zühd, 59: Rızkın kefaleti ve tevekkül. — Bütün canlıların rızkının ilahi kefalet altında olduğunu bilmek, çalışmayı bırakmadan kalbi endişeden kurtarır.",
                    "11. Kaynak: Sahih-i Buhari, Edeb, 27: 'Merhamet etmeyene merhamet olunmaz.' — Tüm mahlukata karşı şefkat ve merhametle yaklaşmak, ilahi rahmete mazhar olmanın şartıdır.",
                    "12. Kaynak: Sahih-i Müslim, Zekat, 52: Vücuttaki her eklem için sadaka. — İnsan bedenindeki yüzlerce eklemin uyumlu çalışması başlı başına bir nimettir ve her gün bunun şükrü mahiyetinde iyilik yapmak gerekir.",
                    "13. Kaynak: Sünen-i Tirmizi, Zühd, 59: Sabır ve şükür dengesi. — Hayatın iniş çıkışlarında sabırla direnmek ve nimetler karşısında şükürle yönelmek, kulun dengesini korur.",
                    "14. Kaynak: Sahih-i Buhari, Tıb, 1: 'Allah bir dert indirdiyse mutlaka şifasını da indirmiştir.' — Hastalık ve arayışların yanında çare ve şifa kanunlarının da yaratıldığını bildirerek ilim ve ümit kapısını açar.",
                    "15. Kaynak: Sünen-i Tirmizi, Sıfatü'l-Kıyamet, 25: Akıllı kişinin nefsini hesaba çekmesi. — Kendi söz, niyet ve amellerini vaktinde muhasebe eden kimse, yarınki büyük hesaba bilinçle hazırlanır.",
                    "16. Kaynak: Müsned-i Şihab: Günlerin kıymeti. — Her yeni doğan günün insana sunduğu imkân ve emanet bilincini hatırlatır.",
                    "17. Kaynak: Sünen-i İbn Mace, Zühd, 22: Haset ve kanaat. — Başkasındakine imrenip haset etmek yerine, kendisine verilen nimetlere kanaat ve şükürle bakmanın huzurunu anlatır.",
                    "18. Kaynak: Sahih-i Buhari, Tevhid, 34: Her varlığın yaratılış gayesine kolaylaştırılması. — Kâinattaki her varlığın kendi fıtratına ve vazifesine uygun şekilde yaratılıp kolaylaştırıldığını ifade eder.",
                    "19. Kaynak: Beyhakî, Şuabü'l-İman: Arı misali faydalı olmak. — Güzel ve temiz olanı alıp şifa ve bereket sunan arı gibi, insandan da etrafına fayda ve güzellik yayılması gerektiğini anlatır.",
                    "20. Kaynak: Sahih-i Müslim, Tevbe, 14: Rahmetin gazabı geçmesi. — İlahi rahmetin genişliğini ve kuşatıcılığını haber vererek kulun ümitsizliğe kapılmadan tövbe ve yönelişle Rabbine dönmesini sağlar."
                ],
                "sages": [
                    "1. Kaynak: Bediüzzaman Said Nursî, Lem'alar (30. Lem'a): Kâinattaki her bir zeytin tanesinde ve zerresinde görülen Samedani sikke. — En küçük bir zeytin tanesinin dahi tüm kâinatı idare eden Samedani kudretin ve birliğin mührünü taşıdığını derinlikli bir tefekkürle ortaya koyar.",
                    "2. Kaynak: Mevlânâ Celâleddîn-i Rûmî, Mesnevi: Karıncanın Süleyman Aleyhisselam'a hediyesi ve samimiyetin değeri. — Küçücük bir çekirge bacağının veya karınca hediyesinin, maddi büyüklükten ziyade samimiyet ve ihlas sebebiyle ne kadar değerli olabileceğini anlatır.",
                    "3. Kaynak: İmam-ı Gazâlî, İhyâü Ulûmi'd-Din: İnsan organlarının ve sistemlerinin mühendislik harikası. — Göz, kalp, sindirim ve sinir sistemlerindeki hassas işleyişi inceleyerek insan bedenindeki ilahi hikmet ve sanatı gözler önüne serer.",
                    "4. Kaynak: Muhyiddin İbn Arabî, Füsûsü'l-Hikem: Varlığın kademelerinde her şeyin kendi hakikatini yaşaması. — Kâinattaki her varlığın kendisine biçilen mertebe ve hikmet dairesinde kendi hakikatini ve vazifesini gerçekleştirdiğini açıklar.",
                    "5. Kaynak: İbrahim Hakkı Erzurumî, Marifetname: Âlem-i sagir (insan) ile âlem-i kebirin (kâinat) mutabakatı. — Küçük âlem sayılan insanın yapısıyla büyük âlem olan kâinat arasındaki derin hikmet ve nizam uyumunu ele alır.",
                    "6. Kaynak: Şâh-ı Nakşibend, Nasihatler: Kalbin uyanıklığı ve her nefiste zikir. — Gaflete düşmeden, her nefeste Hakk'ı hatırlama ve kalbi daima uyanık tutma esasını vurgular.",
                    "7. Kaynak: Yunus Emre, Divan: Hak tecellisinin her zerrede kaim olması. — Varlık sahnesindeki her şeyin Hakk'ın kudret ve hikmetiyle ayakta durduğunu ve anlam kazandığını dile getirir.",
                    "8. Kaynak: Abdülkâdir Geylânî, Fütûhu'l-Gayb: Kulun sabır ve şükürle makamları aşması. — Sabır, şükür ve teslimiyetle kulun nefis engellerini aşıp manevi olgunluğa yükseldiğini anlatır.",
                    "9. Kaynak: İmam-ı Rabbânî, Mektûbât: Zerrelerin dahi Yaratıcı'yı tespih etmesi. — Kâinattaki en küçük zerrelerin bile Yaratıcının emrine boyun eğerek O'nu tespih ettiğini bildirir.",
                    "10. Kaynak: Cüneyd-i Bağdâdî, Kuşeyri Risalesi: Tevhidin ve teslimiyetin hakikati. — Gerçek tevhidin, kulun kendi tedbir ve benlik iddiasını bırakıp Mutlak İradeye teslim olmasıyla kemal bulacağını açıklar.",
                    "11. Kaynak: Beyazıd-i Bistâmî, Tezkiretü'l-Evliya: Nefsin tezkiyesi ve ilahi marifet. — Nefsin arındırılmasının kalbi hakikat ışığına açtığını ve marifetullah yolunu berraklaştırdığını ifade eder.",
                    "12. Kaynak: Hacı Bayrâm-ı Velî, Evrad ve Dualar: Zenginlik ve fakirliğin imtihan sırrı. — Bolluğun da darlığın da kulun kalbini ve şükrünü sınayan ilahi bir imtihan vesilesi olduğunu hatırlatır.",
                    "13. Kaynak: Aziz Mahmud Hüdâyî, Sohbetnâme: Canlıların ve tabiatın fıtri ibadeti. — Hayvanların, bitkilerin ve tabiat unsurlarının kendi yaratılış fıtratları üzere Yaratıcıya boyun eğdiğini anlatır.",
                    "14. Kaynak: Niyâzî-i Mısrî, Divan: Zıtların aynasında ilahi kemalin tecellisi. — Karşıt görünen hâllerin ve zıtlıkların, kâinattaki nizamı ve ilahi hikmeti görünür kıldığını işler.",
                    "15. Kaynak: Sadreddin Konevî, Miftâhü'l-Gayb: Kâinatın vahdet tablosu. — Varlık âleminin dağınık parçalar yığını değil, tek bir Hakikatin hikmetle örülmüş bütünlük tablosu olduğunu gösterir.",
                    "16. Kaynak: Eşrefoğlu Rûmî, Müzekki'n-Nüfûs: Nefis terbiyesi ve ahlâk-ı Muhammediye. — Nefsi terbiye edip güzel ahlakla bezenmenin, hakikat yolculuğunun ayrılmaz bir parçası olduğunu anlatır.",
                    "17. Kaynak: Hasan-ı Basrî, Kelimat-ı Hikmet: Dünyanın geçiciliği ve ahiret bilinci. — Geçici dünya menfaatleri karşısında kalıcı hakikati ve ahiret bilincini diri tutmanın önemini vurgular.",
                    "18. Kaynak: Fudayl bin İyâz, Tabakatü's-Sufiyye: Amellerin en hayırlısının ihlaslı olanı. — Yapılan işin çokluğundan ziyade, yalnızca Allah rızası gözetilerek ve doğru usulle yapılması gerektiğini öğretir.",
                    "19. Kaynak: Sehl et-Tüsterî, Tefsir: Kalp nuru ve marifetullah. — Zikir, tefekkür ve takva ile parlayan kalbin hakikat nurunu daha berrak görebileceğini açıklar.",
                    "20. Kaynak: Ahmed er-Rifâî, İrşadü'l-Müslimîn: Yaratılmışlara şefkat ve merhamet. — Tüm insanlara ve yaratılmışlara karşı şefkatli, yumuşak huylu ve bağışlayıcı olmanın manevi değerini işler."
                ]
            }
        }
    },
    "EN": {
        "app_title": "🌌 Contemplation of the Universe & Unity Consciousness",
        "app_subtitle": "Reading Truth Behind the Veil with Verified Sources & Scientific Reflections",
        "menu_title": "📚 Contemplation Topics",
        "section_title": "📌 Modules & Sections",
        "mod_reflection": "🧠 Deep Reflection & Scientific Data",
        "mod_verses": "📖 Verses with Official Translation (20 Sources)",
        "mod_hadiths": "🕌 Authenticated Hadiths (20 Sources)",
        "mod_sages": "🕊️ Islamic Scholars & Works (20 Sources)",
        "sleep_notice": (
            "💡 *Note:* This web application is hosted on free servers. "
            "It may enter sleep mode after a period of inactivity.\n\n"
            "💤 If you encounter such a screen, click the blue "
            "*'Yes, get this app back up!'* button on the screen and wait 15-30 seconds for it to wake up."
        ),
        "legal_title": "⚖️ LEGAL NOTICE, COPYRIGHT & TERMS OF USE",
        "legal_text": (
            "© 2026 All Rights Reserved. This digital work is created solely for knowledge sharing and spiritual awareness. "
            "Commercial use, copying, reproduction, or distribution without explicit permission and attribution is strictly prohibited."
        ),
        "topics": {
            "1. The Alchemy of Intention & Spreading Goodness Through Technology": {
                "essay": """Every modern tool in human hands—a line of code, a website, or electromagnetic waves—transforms into a vessel of 
divine wisdom and continuous charity when united with pure intention. Just as digital signals travel through the air, 
our intention is for goodness and truth to reach every soul.

Scientific & Empirical Perspective: According to the laws of physics, electromagnetic signals and fiber-optic data 
travel at approximately 300,000 kilometers per second (the speed of light). This physical reality illustrates how rapidly 
and vastly information and intention can propagate across the globe.""",
                "verses": [
                    "1. Quran, Al-Baqarah 261: 'The example of those who spend their wealth in the way of Allah is like a seed [of grain] which grows seven spikes...' (Official Translation)",
                    "2. Quran, Al-Isra 44: 'The seven heavens and the earth and whatever is in them exalt Him. And there is not a thing except that it exalts [Allah] by His praise...' (Official Translation)",
                    "3. Quran, Al-An'am 162: 'Say, 'Indeed, my prayer, my rites of sacrifice, my living and my dying are for Allah, Lord of the worlds.'' (Official Translation)",
                    "4. Quran, Al-Baqarah 115: 'And to Allah belongs the east and the west. So wherever you [might] turn, there is the Face of Allah...' (Official Translation)",
                    "5. Quran, Ar-Ra'd 15: 'And to Allah prostrates whoever is within the heavens and the earth, willingly or unwillingly, and their shadows...' (Official Translation)",
                    "6. Quran, Al-Hijr 29: 'And when I have proportioned him and breathed into him of My created soul, then fall down to him in prostration.' (Official Translation)",
                    "7. Quran, Al-Hadid 4: 'It is He who created the heavens and earth in six days and then established Himself above the Throne... And He is with you wherever you are.' (Official Translation)",
                    "8. Quran, Qaf 16: 'And We have already created man and know what his soul whispers to him, and We are closer to him than [his] jugular vein.' (Official Translation)",
                    "9. Quran, Adh-Dhariyat 56: 'And I did not create the jinn and mankind except to worship Me.' (Official Translation)",
                    "10. Quran, Al-Isra 70: 'And We have certainly honored the children of Adam and carried them on the land and sea and provided for them of the good things...' (Official Translation)",
                    "11. Quran, Al-Mulk 3: '[He] who created seven heavens in layers. You do not see in the creation of the Most Merciful from inconsistency...' (Official Translation)",
                    "12. Quran, Al-Qamar 49: 'Indeed, all things We created with predestination (measure).' (Official Translation)",
                    "13. Quran, Al-Baqarah 216: 'But perhaps you hate a thing and it is good for you; and perhaps you love a thing and it is bad for you. And Allah knows, while you know not.' (Official Translation)",
                    "14. Quran, Al-Anbiya 35: 'Every soul will taste death. And We test you with evil and with good as trial, and to Us you will be returned.' (Official Translation)",
                    "15. Quran, Ash-Sharh 5-6: 'For indeed, with hardship [will be] ease. Indeed, with hardship [will be] ease.' (Official Translation)",
                    "16. Quran, An-Nahl 18: 'And if you should count the favors of Allah, you could not enumerate them...' (Official Translation)",
                    "17. Quran, Ibrahim 7: 'And [remember] when your Lord proclaimed, 'If you are grateful, I will surely increase you [in favor]...'' (Official Translation)",
                    "18. Quran, An-Nur 35: 'Allah is the Light of the heavens and the earth...' (Official Translation)",
                    "19. Quran, Al-Anfal 17: 'And you did not kill them, but it was Allah who killed them. And you did not throw when you threw, but it was Allah who threw...' (Official Translation)",
                    "20. Quran, Al-Kahf 110: 'Say, 'I am only a man like you, to whom has been revealed that your god is one God. So whoever would hope for the meeting with his Lord - let him do righteous work...'' (Official Translation)"
                ],
                "hadiths": [
                    "1. Source: Sahih al-Bukhari 1, Sahih Muslim 1907: 'Actions are judged by intentions...' — Every deed and tool gains its spiritual weight from the sincerity of the intention behind it, turning even digital effort into meaningful service.",
                    "2. Source: Sahih Muslim 1631: 'When a human dies, their deeds cease except for three...' — Beneficial knowledge shared openly can continue bearing fruit as ongoing charity long after the moment it was created.",
                    "3. Source: Sahih Muslim 1893: 'Whoever guides to a good has a reward like its doer.' — Opening a door to goodness and guiding others toward truth shares in the reward of every step taken.",
                    "4. Source: Sahih al-Bukhari 47, Sahih Muslim 8: Hadith of Gabriel on Ihsan. — Acting with excellence and mindfulness, knowing that Allah sees every action even when unseen by the eye, elevates ordinary work into devotion.",
                    "5. Source: Sahih Muslim 2999: 'Wondrous is the affair of the believer...' — Gratitude in ease and patience in hardship turn every circumstance into spiritual growth.",
                    "6. Source: Sunan an-Nasa'i 324: 'Whoever does not thank people has not thanked Allah.' — Acknowledging those who help or serve as channels of good is an essential step toward gratitude to the Creator.",
                    "7. Source: Sahih Muslim 2564: 'Indeed Allah does not look at your bodies or forms, but at your hearts.' — Inner sincerity and genuine devotion matter far more than outward appearances or status.",
                    "8. Source: Sahih Muslim 54: 'You will not enter Paradise until you believe...' — Mutual love and compassion among believers nurture hearts aligned with truth.",
                    "9. Source: Jami' at-Tirmidhi 1956: 'Your smile for your brother is charity.' — A warm smile and gentle manner are simple yet genuine acts of everyday kindness.",
                    "10. Source: Sahih al-Bukhari 438, Sahih Muslim 521: 'The earth has been made for me a mosque and pure.' — Every place on earth becomes a space of reverence and mindfulness when approached with awareness.",
                    "11. Source: Sahih Muslim 482: 'The closest a servant is to his Lord is when he is prostrating.' — Laying down the ego in prostration marks the deepest state of humility and closeness to the Divine.",
                    "12. Source: Jami' at-Tirmidhi 3383: Best remembrance and gratitude. — Remembrance of God's oneness and gratitude for His blessings anchor the heart in clarity and thankfulness.",
                    "13. Source: Sahih al-Bukhari 6407: The example of one who remembers Allah. — Remembering the Creator brings spiritual life and wakefulness to the heart, much like life compared to lifelessness.",
                    "14. Source: Sahih Muslim 91: 'No one with an atom of pride will enter Paradise.' — Pride veils the heart from truth, whereas humility clears the way for wisdom and grace.",
                    "15. Source: Sahih Muslim 2588: Humility elevates one before Allah. — Humility before God does not diminish a person; rather, it elevates them in true dignity.",
                    "16. Source: Sahih al-Bukhari 69, Sahih Muslim 1734: 'Facilitate and do not make difficult.' — Sharing knowledge and guidance should ease burdens, inspire hope, and draw people closer rather than alienate them.",
                    "17. Source: Al-Mu'jam al-Awsat 5787: 'The best of people are those most beneficial to others.' — The value of knowledge, skill, and effort is measured by the genuine benefit it brings to others.",
                    "18. Source: Sahih al-Bukhari 6023: 'A good word is charity.' — Kind, constructive, and truthful speech spreads goodwill and eases human hearts.",
                    "19. Source: Sahih al-Bukhari 6416: 'Be in this world as if you were a stranger or a traveler.' — Living as a traveler in this world keeps attachment light and focus clear on lasting purpose.",
                    "20. Source: Jami' at-Tirmidhi 3391: Rewards of morning and evening remembrance. — Anchoring the morning and evening with remembrance protects the inner state throughout the day."
                ],
                "sages": [
                    "1. Source: Al-Ghazali, Ihya Ulum al-Din: The universe is a grand book written by Divine Power. — Every phenomenon in creation serves as a readable sign pointing to the wisdom, order, and power of its Maker.",
                    "2. Source: Rumi, Masnavi (Vol. 1): 'Whatever is in the pitcher spills out.' — What fills the inner heart and intention naturally overflows into words, deeds, and creation.",
                    "3. Source: Ibn Arabi, Fusus al-Hikam: Every form is a mirror of divine knowledge. — Created forms reflect aspects of divine wisdom and beauty according to their capacity and station.",
                    "4. Source: Yunus Emre, Divan: 'We love the created for the Creator's sake.' — Loving creation with mercy and reverence flows from recognizing the Creator's imprint in all things.",
                    "5. Source: Abdul-Qadir Gilani, Sirr al-Asrar: When ego fades, the True Doer is witnessed. — Stepping back from self-centered claims allows the heart to recognize the true Source of power and grace.",
                    "6. Source: Imam Rabbani, Maktubat (Vol. 1): Seeing causes as veils and God as the Causer. — Secondary causes and tools operate by divine command while remaining veils behind which the true Causer acts.",
                    "7. Source: Baha'ud-Din Naqshband, Risala-i Qudsiyya: Solitude in the crowd ('Halvet der encümen'). — Maintaining inner presence and remembrance of God even while engaged actively in daily life and society.",
                    "8. Source: Ibrahim Hakki Erzurumi, Marifetname: Divine turning of hardships into ease. — Difficulties and trials can become openings for wisdom and relief through trust and awareness.",
                    "9. Source: Junayd of Baghdad, Al-Risala al-Qushayriyya: Tawhid and annihilation of self. — True unity consciousness deepens as egoistic self-assertion dissolves before the One.",
                    "10. Source: Bayazid Bastami, Tadhkirat al-Awliya: The Seeker and Sought are His grace. — Every step of seeking and every glimpse of understanding are made possible by prior divine grace.",
                    "11. Source: Haci Bayram Veli: 'He who knows himself knows his Lord.' — Contemplating one's own frailty, design, and dependence leads directly to recognizing the Lord.",
                    "12. Source: Aziz Mahmud Hudayi, Sohbetname: The remembrance of atoms. — Even the tiniest particles in the cosmos fulfill their appointed order in continuous remembrance of their Maker.",
                    "13. Source: Niyazi Misri, Divan: Creation as a mirror. — The visible world acts as a mirror in which signs of inner meaning and divine attributes are reflected.",
                    "14. Source: Sadr al-Din al-Qunawi, Miftah al-Ghayb: Harmony of atom and sphere. — Explores the coherent order linking micro-level existence with the grand cosmic spheres.",
                    "15. Source: Said Nursi, Risale-i Nur (The Words - 33rd Word): The universe as a vast mosque. — Views the cosmos as a grand sanctuary filled with voices of praise, order, and reflection pointing to its Creator.",
                    "16. Source: Esrefoglu Rumi, Muzekki al-Nufus: Polishing the heart through praise. — Remembrance, gratitude, and self-discipline polish the heart so it reflects truth clearly.",
                    "17. Source: Hasan al-Basri, Hikmah sayings: Intention surpasses action in blessing. — Sincere intention gives depth and enduring value to outward deeds.",
                    "18. Source: Fudayl ibn Iyad, Tabaqat al-Sufiyya: Sincerity (Ihlas). — Emphasizes that deeds are accepted and meaningful to the extent they are pure in motive and aligned with right guidance.",
                    "19. Source: Sahl al-Tustari, Tafsir: Heartfelt presence as supreme remembrance. — Attentive presence of the heart gives remembrance its living depth and spiritual warmth.",
                    "20. Source: Ahmed al-Rifa'i, Irshad al-Muslimin: Compassion born of recognizing human weakness. — Recognizing shared human fragility fosters mercy, gentleness, and forgiveness toward others."
                ]
            },
            "2. Universal Remembrance, Salawat & Continuous Prostration": {
                "essay": """Prostration is not merely a physical ritual; it is the state of annihilating the ego and consciously joining 
the uninterrupted worship of the cosmos. Walking, breathing, and immersing in water align us with the elementals' prostration.

Scientific & Empirical Perspective: Biophysics confirms that human bodies constantly experience atmospheric pressure, 
gravity (9.81 m/s²), and hydrodynamic forces. Skin contact with air and a body water composition of 60-70% reflect 
direct physical interaction with the elemental ecosystem.""",
                "verses": [
                    "1. Quran, Ar-Ra'd 15: 'And to Allah prostrates whoever is within the heavens and the earth, willingly or unwillingly, and their shadows...' (Official Translation)",
                    "2. Quran, Al-Hajj 18: 'Do you not see that to Allah prostrates whoever is in the heavens and whoever is on the earth and the sun, the moon, the stars, the mountains, the trees, the moving creatures and many of the people?' (Official Translation)",
                    "3. Quran, An-Nahl 49: 'And to Allah prostrates whatever is in the heavens and whatever is on the earth of creatures, and the angels [as well], and they are not arrogant.' (Official Translation)",
                    "4. Quran, Al-Ahzab 56: 'Indeed, Allah and His angels confer blessing upon the Prophet. O you who have believed, ask [Allah to confer] blessing upon him and ask [Him to grant him] peace.' (Official Translation)",
                    "5. Quran, Al-Isra 44: 'The seven heavens and the earth and whatever is in them exalt Him...' (Official Translation)",
                    "6. Quran, An-Nur 41: 'Do you not see that Allah is exalted by whomever is within the heavens and the earth and [even] the birds with wings spread out? Each [of them] has known his [means of] prayer and his exalting...' (Official Translation)",
                    "7. Quran, Al-Anbiya 79: '...And We subjected the mountains to exalt [Us], along with David and the birds...' (Official Translation)",
                    "8. Quran, Al-Hashr 24: 'He is Allah, the Creator, the Inventor, the Fashioner; to Him belong the best names. Whatever is in the heavens and earth is exalting Him...' (Official Translation)",
                    "9. Quran, Jumu'ah 1: 'Whatever is in the heavens and whatever is on the earth is exalting Allah, the Sovereign, the Pure, the Exalted in Might, the Wise.' (Official Translation)",
                    "10. Quran, At-Taghabun 1: 'Whatever is in the heavens and whatever is on the earth is exalting Allah. To Him belongs dominion, and to Him belongs [due] praise...' (Official Translation)",
                    "11. Quran, Al-Alaq 19: 'No! Do not obey him. But prostrate and draw near [to Allah].' (Official Translation)",
                    "12. Quran, Al-A'raf 206: 'Indeed, those who are near your Lord are not too proud to worship Him, and they exalt Him, and to Him they prostrate.' (Official Translation)",
                    "13. Quran, As-Sajdah 15: 'Only those believe in Our verses who, when they are reminded by them, fall down in prostration and exalt [Allah] with praise of their Lord...' (Official Translation)",
                    "14. Quran, Al-Furqan 64: 'And those who spend [part of] the night to their Lord prostrating and standing [in prayer].' (Official Translation)",
                    "15. Quran, Al-Fath 29: '...Their mark is on their faces from the trace of prostration...' (Official Translation)",
                    "16. Quran, Al-Baqarah 152: 'So remember Me; I will remember you. And be grateful to Me and do not deny Me.' (Official Translation)",
                    "17. Quran, Al-Ahzab 41-42: 'O you who have believed, remember Allah with much remembrance. And exalt Him morning and afternoon.' (Official Translation)",
                    "18. Quran, Ar-Ra'd 28: 'Those who have believed and whose hearts find rest in the remembrance of Allah. Unquestionably, by the remembrance of Allah hearts are assured.' (Official Translation)",
                    "19. Quran, Ta-Ha 14: 'Indeed, I am Allah. There is no deity except Me, so worship Me and establish prayer for My remembrance.' (Official Translation)",
                    "20. Quran, Al-Ankabut 45: '...And the remembrance of Allah is greater...' (Official Translation)"
                ],
                "hadiths": [
                    "1. Source: Sahih Muslim 482: 'The closest a servant is to his Lord is when he is prostrating.' — Prostration represents the highest spiritual closeness as the servant places forehead and ego low before the Lord.",
                    "2. Source: Sahih Muslim 408: 'Whoever sends blessings upon me once, Allah sends ten upon him.' — Sending salawat expresses love and honor for the Prophet while opening abundant mercy upon the one who sends it.",
                    "3. Source: Sahih al-Bukhari 438, Sahih Muslim 521: The earth made pure and a mosque. — The earth is purified as a place of worship and prostration, linking everyday ground with sacred awareness.",
                    "4. Source: Sahih Muslim 225: Prostration raises one in rank. — Every prostration undertaken for Allah elevates a person's station and wipes away shortcomings.",
                    "5. Source: Sahih Muslim 489: Advice to Rabi'ah b. Ka'b. — When asked for companionship in paradise, the Prophet advised helping through frequent prostration, underscoring its central role in devotion.",
                    "6. Source: Jami' at-Tirmidhi 3375: Keeping the tongue moist with remembrance. — Encourages continuous remembrance of God woven naturally into daily moments rather than confined to rare occasions.",
                    "7. Source: Sahih al-Bukhari 6406: Two light phrases heavy on the scale. — Words of glorification and praise that are light on the tongue yet carry immense weight on the scale of deeds.",
                    "8. Source: Sahih Muslim 2699: Gathering for remembrance and angels. — Gatherings centered on remembrance and reflection are surrounded by angels and enveloped in tranquility and mercy.",
                    "9. Source: Sunan Abu Dawud 1047: Increasing Salawat on Fridays. — Highlights Friday as a special time to multiply salutations upon the Prophet.",
                    "10. Source: Jami' at-Tirmidhi 484: Those closest on Judgment Day. — Closeness on the Day of Judgment belongs to those with the finest character and devotion.",
                    "11. Source: Musnad Ahmad: Echoing praise. — Points to the harmonious resonance of glorification across creation and believers.",
                    "12. Source: Sunan Abu Dawud 5051: Purity before sleep. — Entering sleep in a state of purity and remembrance safeguards the soul through rest.",
                    "13. Source: Sahih Muslim 2165: Walking with humility. — Walking with quiet dignity and humility reflects harmony with the order of creation.",
                    "14. Source: Jami' at-Tirmidhi 3598: Weight of glorification. — Glorifying and magnifying God strengthens the heart and anchors it in awe and gratitude.",
                    "15. Source: Sunan Abu Dawud 1090: Prayers during natural phenomena. — Turning to prayer and remembrance during winds, rain, and natural events awakens awareness of divine power.",
                    "16. Source: Sunan Ibn Majah 425: Water conservation. — Prohibiting waste of water even beside a flowing river teaches mindfulness and moderation toward natural blessings.",
                    "17. Source: Sahih al-Bukhari 807: Dissolving ego through prostration. — Prostration humbles self-importance and softens the heart before divine majesty.",
                    "18. Source: Sahih Muslim 758: Night prayer. — Standing and prostrating in the quiet of night cultivates inner light and serenity.",
                    "19. Source: Shu'ab al-Iman: Believer's contemplation. — Thoughtful observation of creation opens the heart to deeper faith and recognition of God.",
                    "20. Source: Al-Mu'jam al-Kabir: Value of contemplation. — Deep reflection on creation carries lasting spiritual value and keeps the heart awake."
                ],
                "sages": [
                    "1. Source: Rumi, Fihi Ma Fih: Every spinning atom dances in love. — Describes every particle and motion under the celestial dome as moving in rhythmic harmony and devotion.",
                    "2. Source: Ibn Arabi, Futuhat al-Makkiyya: The cosmos as a sanctuary. — Views the entire universe as a place of prostration and servitude before the Creator.",
                    "3. Source: Yunus Emre, Risalat al-Nushiyya: Calling upon the Lord with nature. — Depicts mountains, streams, and creation joining in remembrance of the Lord.",
                    "4. Source: Al-Ghazali, Kimiya-i Sa'adat: True prostration of the heart. — Teaches that true prostration unites bodily posture with the surrender and humility of the heart.",
                    "5. Source: Ibrahim Hakki Erzurumi, Marifetname: Cosmic orchestra. — Portrays creation as a coordinated symphony guided by one Supreme Wisdom.",
                    "6. Source: Abdul-Qadir Gilani, Jila al-Khatir: Eternal prostration of the soul. — Urges keeping the inner orientation of the soul bowed in devotion even amid worldly tasks.",
                    "7. Source: Junayd of Baghdad: Annihilation in remembrance. — Describes self-forgetfulness in remembrance where awareness centers on the One remembered.",
                    "8. Source: Shams Tabrizi, Makalat: Moving the shadow aside. — Calls for setting aside passing shadows of ego to perceive lasting reality.",
                    "9. Source: Said Nursi, Letters (20th Letter): Praise from atoms to stars. — Explains how every entity from tiny atoms to vast stars glorifies its Creator through its order and existence.",
                    "10. Source: Niyazi Misri, Maktubat: Gnosis and remembrance. — Emphasizes that remembrance should awaken inner insight and spiritual awareness.",
                    "11. Source: Haci Bektas Veli, Makalat: Beauty and perfection. — Points to the mystery of beauty and moral perfection in the path of spiritual refinement.",
                    "12. Source: Aziz Mahmud Hudayi, Nafais al-Majalis: Air particle remembrance. — Notes that even minute particles in the air follow their appointed order in remembrance of God.",
                    "13. Source: Bayazid Bastami: Worship from His grace. — Recognizes that true devotion and access to worship come through divine grace.",
                    "14. Source: Imam Rabbani, Maktubat: Light of prophetic adherence. — Highlights following the prophetic example and sending salawat as a source of spiritual light.",
                    "15. Source: Esrefoglu Rumi, Tarikatname: Joining natural praise. — Encourages conscious participation in the praise that pervades the natural world.",
                    "16. Source: Mansur al-Hallaj, Kitab al-Tawasin: Unity and awareness. — Explores the journey toward witnessing unity and deeper spiritual consciousness.",
                    "17. Source: Sadr al-Din al-Qunawi: Prostration of shadows. — Reflects on how shifting shadows and natural cycles bear witness to divine rule.",
                    "18. Source: Ahmad Yasawi, Divan-i Hikmet: Dawn remembrance. — Celebrates the quiet clarity and spiritual renewal of remembrance at dawn.",
                    "19. Source: Farid al-Din Attar, Mantiq al-Tayr: Praise of creation. — Weaves a symbolic journey showing all creatures moving according to their nature and longing toward truth.",
                    "20. Source: Ken'an Rifai, Sohbetler: Carrying prayer into the world. — Stresses carrying the spirit and reverence of prayer out into daily life and human relationships."
                ]
            },
            "3. The Seal of Oneness, the Ant & the Sun, and the Wisdom of Opposites": {
                "essay": """The universe is a three-dimensional veil revealing the Absolute Power behind it. Upon this veil, from the smallest atom 
to the largest galaxy, rests the "Seal of Oneness" (Ehadiyet) of the same Master Artist. The sun cannot match the biological 
artistry of an ant, nor can the ant perform the sun's cosmic duties.

Scientific & Empirical Perspective: Biology and entomology demonstrate that ants (Formicidae) can carry 20 to 50 times 
their body weight, showcasing a remarkable mechanical and hydraulic design. Meanwhile, the sun functions as a massive nuclear 
fusion reactor devoid of consciousness. In human physiology, homeostasis and autonomic nervous systems maintain vital functions 
even during sleep, proving continuous divine care.""",
                "verses": [
                    "1. Quran, Al-Ikhlas 1-2: 'Say, 'He is Allah, [who is] One. Allah, the Eternal Refuge.'' (Official Translation)",
                    "2. Quran, An-Naml 18: 'Until, when they came upon the valley of the ants, an ant said, 'O ants, enter your dwellings that you not be crushed by Solomon and his soldiers while they perceive not.'' (Official Translation)",
                    "3. Quran, Ya-Sin 38-40: 'And the sun runs [on a course] for a determined term for it... And the moon - We have determined for it phases... It is not allowed for the sun to reach the moon, nor does the night outstrip the day. Each, in an orbit, is swimming.' (Official Translation)",
                    "4. Quran, Al-Baqarah 30: 'And [mention, O Muhammad], when your Lord said to the angels, 'Indeed, I will make upon the earth a successive authority...'' (Official Translation)",
                    "5. Quran, At-Tin 4: 'We have certainly created man in the best of stature.' (Official Translation)",
                    "6. Quran, Al-Jathiyah 13: 'And He has subjected to you whatever is in the heavens and whatever is on the earth - all from Him. Indeed in that are signs for a people who give thought.' (Official Translation)",
                    "7. Quran, Al-Mulk 2: '[He] who created death and life to test you [as to] which of you is best in deed - and He is the Exalted in Might, the Forgiving.' (Official Translation)",
                    "8. Quran, Al-Anbiya 35: 'Every soul will taste death. And We test you with evil and with good as trial...' (Official Translation)",
                    "9. Quran, Ash-Shams 7-10: 'And [by] the soul and He who proportioned it... He has succeeded who purifies it.' (Official Translation)",
                    "10. Quran, Ar-Rahman 7-9: 'And the heaven He raised and imposed the balance that you not transgress within the balance. And establish weight in justice and do not make deficient the balance.' (Official Translation)",
                    "11. Quran, Al-Furqan 2: '[He] to whom belongs the dominion of the heavens and the earth and who has not taken a son and has not had a partner in dominion and has created each thing and determined it with [precise] determination.' (Official Translation)",
                    "12. Quran, Az-Zumar 9: '...Say, 'Are those who know equal to those who do not know?' Only they will remember who are people of understanding.' (Official Translation)",
                    "13. Quran, Al-Baqarah 164: 'Indeed, in the creation of the heavens and the earth, and the alternation of the night and the day, and the ships which sail through the sea with that which benefits people... are signs for a people who use reason.' (Official Translation)",
                    "14. Quran, Ar-Rum 22: 'And of His signs is the creation of the heavens and the earth and the diversity of your languages and your colors. Indeed in that are signs for those of knowledge.' (Official Translation)",
                    "15. Quran, Hud 6: 'And there is no creature on earth but that upon Allah is its provision, and He knows its place of dwelling and place of storage...' (Official Translation)",
                    "16. Quran, Al-An'am 38: 'And there is no creature on [or within] the earth or a bird that flies with its wings except [that they are] communities like you...' (Official Translation)",
                    "17. Quran, As-Sajdah 7: 'Who perfected everything which He created and began the creation of man from clay.' (Official Translation)",
                    "18. Quran, Adh-Dhariyat 20-21: 'And on the earth are signs for the certain [in faith] And in yourselves. Then will you not see?' (Official Translation)",
                    "19. Quran, Al-Ghashiyah 17-20: 'Then do they not look at the camels - how they are created? And at the sky - how it is raised? And at the mountains - how they are erected? And at the earth - how it is spread out?' (Official Translation)",
                    "20. Quran, Ali 'Imran 191: 'Who remember Allah while standing or sitting or [lying] on their sides and give thought to the creation of the heavens and the earth...' (Official Translation)"
                ],
                "hadiths": [
                    "1. Source: Sahih Muslim 147: 'Indeed Allah is Beautiful and loves beauty.' — The beauty, proportion, and harmony in creation reflect the One who is Beautiful and loves beauty.",
                    "2. Source: Sahih al-Bukhari 5641: Believers learning and growing from trials. — Trials become instruments of spiritual growth and clarity when met with patience and reflection.",
                    "3. Source: Sunan Ibn Majah 224: 'Seeking knowledge is an obligation upon every Muslim.' — Pursuing beneficial knowledge is essential to understanding both faith and the wisdom woven into creation.",
                    "4. Source: Al-Maqasid al-Hasana: 'He who knows himself knows his Lord.' — Contemplating one's own design, dependence, and inner life leads to deeper recognition of the Creator.",
                    "5. Source: Sahih al-Bukhari 3319: Prohibition of harming ants and animals. — Forbidding needless harm even to small creatures like ants reflects reverence for life and divine craftsmanship.",
                    "6. Source: Jami' at-Tirmidhi 2398: Trials proportional to faith. — Hardships correspond to faith and capacity, revealing wisdom and measure in how trials are apportioned.",
                    "7. Source: Sahih al-Bukhari 6412: Two blessings squandered: health and free time. — Health and free time are vital blessings that call for mindful gratitude and constructive use.",
                    "8. Source: Sunan Ibn Majah 1385: Gratitude for sleep and waking. — Waking and resting each day is a recurring blessing that invites thankfulness for life and renewal.",
                    "9. Source: Al-Mu'jam al-Awsat: Value of an hour of contemplation. — Sincere reflection on creation holds deep spiritual worth in awakening insight.",
                    "10. Source: Jami' at-Tirmidhi 2344: Reliance on Allah and sustenance. — True reliance combines earnest effort with trust in God's provision.",
                    "11. Source: Sahih al-Bukhari 6013: 'He who does not show mercy will not be shown mercy.' — Mercy extended to others is the key to receiving mercy.",
                    "12. Source: Sahih Muslim 720: Daily charity for every joint. — Every joint and function of the body is a daily gift warranting gratitude and acts of kindness.",
                    "13. Source: Jami' at-Tirmidhi 2400: Patience and gratitude. — Patience in difficulty and gratitude in blessing form the steady balance of a believer's life.",
                    "14. Source: Sahih al-Bukhari 5678: Every disease has a cure. — Afflictions are accompanied by remedies within creation, encouraging inquiry, care, and hope.",
                    "15. Source: Jami' at-Tirmidhi 2459: The smart person holds himself accountable. — Self-examination and mindful accountability prepare a person for what comes next.",
                    "16. Source: Al-Shihab: Value of each new day. — Each passing day carries precious opportunities for good deeds and conscious reflection.",
                    "17. Source: Jami' at-Tirmidhi 2465: Contentment versus envy. — Contentment with what is allotted brings inner peace, whereas envy breeds restlessness.",
                    "18. Source: Sahih al-Bukhari 4940: Every creature facilitated for its purpose. — Each created being is guided and equipped for the role for which it was made.",
                    "19. Source: Shu'ab al-Iman: Being like the honeybee. — Like the honeybee that feeds on what is pure and produces what is beneficial, a believer brings goodness without harm.",
                    "20. Source: Sahih Muslim 2751: Divine mercy exceeding wrath. — God's mercy encompasses and surpasses His wrath, opening the door to hope and repentance."
                ],
                "sages": [
                    "1. Source: Said Nursi, The Words (33rd Word): The Seal of Oneness in atoms and flowers. — Demonstrates how every atom and living form bears the unified signature of the One Creator.",
                    "2. Source: Rumi, Masnavi: Wisdom of opposites. — Explains how contrasts and opposites give movement, perception, and meaning to existence.",
                    "3. Source: Al-Ghazali, Ihya: Human biology and sleep miracles. — Highlights the intricate design of human organs and the restorative wonder of sleep as signs of divine wisdom.",
                    "4. Source: Ibn Arabi, Fusus: Flaws as dark pigments in a masterpiece. — Compares seemingly dark or difficult elements to deeper tones that complete a larger artistic composition.",
                    "5. Source: Ibrahim Hakki Erzurumi, Marifetname: Macrocosm in an atom. — Explores how the order of the microcosm mirrors and connects with the larger cosmos.",
                    "6. Source: Baha'ud-Din Naqshband: Acceptance in trials. — Emphasizes tranquil acceptance and trust when facing trials.",
                    "7. Source: Yunus Emre, Divan: True power belongs to the Creator. — Affirms that all power and agency in creation trace back to the Creator.",
                    "8. Source: Abdul-Qadir Gilani, Gunyat al-Talibin: Hardships as honored guests. — Encourages receiving hardships with patience and spiritual poise rather than despair.",
                    "9. Source: Imam Rabbani, Maktubat: All entities as obedient servants. — Describes created things as dutiful servants acting within their appointed bounds.",
                    "10. Source: Sadr al-Din al-Qunawi: The manifestation of Oneness. — Examines how unity is manifested across the levels of existence.",
                    "11. Source: Junayd of Baghdad: Wisdom in withholding. — Notes that what is withheld can hold hidden wisdom and protection.",
                    "12. Source: Haci Bayram Veli: Humanity as the cosmic fruit. — Sees humanity's capacity for consciousness and love as the ripened fruit of creation.",
                    "13. Source: Bayazid Bastami: Mercy hidden within trials. — Points to concealed mercy and spiritual benefit present even inside trials.",
                    "14. Source: Niyazi Misri, Divan: The three-dimensional veil. — Invites looking beyond outward three-dimensional forms toward deeper spiritual meaning.",
                    "15. Source: Esrefoglu Rumi, Muzekki al-Nufus: Awakening from heedlessness. — Calls for awakening the heart from heedlessness through purification and remembrance.",
                    "16. Source: Aziz Mahmud Hudayi: Atoms fulfilling duties. — Depicts atoms faithfully carrying out their designated duties in creation.",
                    "17. Source: Farid al-Din Attar: Discipline of the ant. — Uses the ant's persistence and discipline as a lesson in steady endeavor.",
                    "18. Source: Hasan al-Basri: Life as passing days. — Reminds that life consists of passing days, urging mindful use of time.",
                    "19. Source: Sahl al-Tustari, Tafsir: True gratitude for blessings. — Defines genuine gratitude as recognizing the Giver and using blessings rightly.",
                    "20. Source: Ken'an Rifai, Sohbetler: Purification through the crucible of fire. — Describes how endurance and trials refine character like metal tested in fire."
                ]
            }
        }
    }
}

# Oturum Durumu Başlangıcı
if "lang" not in st.session_state:
    st.session_state.lang = "TR"

# Sol Menü (Sidebar)
with st.sidebar:
    lang_choice = st.radio(
        "🌐 Dil / Language",
        options=["TR", "EN"],
        format_func=lambda x: "🇹🇷 Türkçe" if x == "TR" else "🇬🇧 English",
        horizontal=True
    )
    st.session_state.lang = lang_choice
    T = DATA[st.session_state.lang]

    st.markdown("---")
    st.subheader(T["menu_title"])
    selected_topic = st.radio(
        label="Topics",
        options=list(T["topics"].keys()),
        label_visibility="collapsed"
    )

    st.sidebar.markdown("---")
    st.sidebar.info(T["sleep_notice"])

    st.markdown(f"""
    <div class="legal-box">
        <strong>{T['legal_title']}</strong><br><br>
        {T['legal_text']}
    </div>
    """, unsafe_allow_html=True)

# Başlıklar
st.title(T["app_title"])
st.caption(T["app_subtitle"])
st.markdown("---")

topic_data = T["topics"][selected_topic]
st.header(selected_topic)

# SOL TARAFTA ALT ALTA SIRALANAN MÖDÜLLER / BÖLÜMLER
st.markdown(f'<p class="module-header">{T["section_title"]}</p>', unsafe_allow_html=True)

selected_module = st.radio(
    "Modüller",
    [
        T["mod_reflection"],
        T["mod_verses"],
        T["mod_hadiths"],
        T["mod_sages"]
    ],
    label_visibility="collapsed"
)

st.markdown("---")

# Seçilen Modüle Göre İçeriği Gösterme
if selected_module == T["mod_reflection"]:
    st.markdown(f"""
    <div class="main-card">
        <p style="font-size: 1.08rem; line-height: 1.85; white-space: pre-line;">{topic_data['essay'].strip()}</p>
    </div>
    """, unsafe_allow_html=True)

elif selected_module == T["mod_verses"]:
    st.markdown(f"### {T['mod_verses']}")
    for item in topic_data["verses"]:
        st.markdown(f'<div class="quote-box">{item}</div>', unsafe_allow_html=True)

elif selected_module == T["mod_hadiths"]:
    st.markdown(f"### {T['mod_hadiths']}")
    for item in topic_data["hadiths"]:
        st.markdown(f'<div class="quote-box">{item}</div>', unsafe_allow_html=True)

elif selected_module == T["mod_sages"]:
    st.markdown(f"### {T['mod_sages']}")
    for item in topic_data["sages"]:
        st.markdown(f'<div class="quote-box">{item}</div>', unsafe_allow_html=True)

# Alt Bilgi
st.markdown(f"""
<div class="legal-box" style="text-align: center;">
    <strong>{T['legal_title']}</strong> — {T['legal_text']}
</div>
""", unsafe_allow_html=True)
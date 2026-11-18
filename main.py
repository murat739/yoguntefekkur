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
                    "1. Kaynak: Sahih-i Buhari, Bedaü'l-Vahy, 1; Sahih-i Müslim, İmare, 155: 'Ameller ancak niyetlere göredir; herkese niyeti vardır.'",
                    "2. Kaynak: Sahih-i Müslim, Cenaiz, 14; Sünen-i Tirmizi, Hubut, 2: 'İnsan ölünce amelleri kesilir; ancak üç şey müstesnadır: Sadaka-i cariye, faydalanılan ilim ve kendisine dua eden salih evlat.'",
                    "3. Kaynak: Sahih-i Müslim, İmare, 133; Sünen-i Ebu Davud, Edeb, 115: 'Hayra vesile olan, hayrı yapan gibidir.'",
                    "4. Kaynak: Sahih-i Buhari, İman, 37; Sahih-i Müslim, İman, 1: Cibril Hadisi olarak bilinen rivayette ihsanın tarifi yapılmıştır.",
                    "5. Kaynak: Sahih-i Müslim, Zühd, 64: 'Müminin durumu ne gariptir; her işi onun için bir hayırdır...'",
                    "6. Kaynak: Sünen-i Tirmizi, Birr, 35: 'İnsanlara teşekkür etmeyen kimse Allah'a da şükretmemiştir.'",
                    "7. Kaynak: Sahih-i Müslim, Birr, 33: 'Şüphesiz Allah sizin suretlerinize ve mallarınıza bakmaz, ancak kalplerinize ve amellerinize bakar.'",
                    "8. Kaynak: Sahih-i Müslim, İman, 71-72: 'İman etmedikçe cennete giremezsiniz, birbirinizi sevmedikçe de gerçek iman etmiş olamazsınız.'",
                    "9. Kaynak: Sünen-i Tirmizi, Birr, 36: 'Din kardeşine tebessüm etmen bir sadakadır.'",
                    "10. Kaynak: Sahih-i Buhari, Salat, 56; Sahih-i Müslim, Mesacid, 3: 'Yeryüzü bana mescit ve temiz kılınmıştır.'",
                    "11. Kaynak: Sahih-i Müslim, Salat, 215: 'Kulun Rabbine en yakın olduğu an secde hâlidir; bu nedenle duayı çoğaltın.'",
                    "12. Kaynak: Sünen-i Tirmizi, Daavat, 9: 'Zikrin en efdali lâ ilâhe illallah, duânın en efdali elhamdülillah'tır.'",
                    "13. Kaynak: Sahih-i Buhari, Deavat, 66: 'Rabbini zikreden ile zikretmeyenin misali, diri ile ölü gibidir.'",
                    "14. Kaynak: Sahih-i Müslim, İman, 147: 'Kalbinde zerre miktarı kibir olan kimse cennete giremez.'",
                    "15. Kaynak: Sahih-i Müslim, Birr, 69: 'Kim Allah için tevazu gösterirse, Allah onu yüceltir.'",
                    "16. Kaynak: Sahih-i Buhari, İlim, 11; Müslim, Cihad, 4: 'Kolaylaştırınız, zorlaştırmayınız; müjdeleyiniz, nefret ettirmeyiniz.'",
                    "17. Kaynak: Taberani, Mu'cemü'l-Evsat, 6/309: 'İnsanların en hayırlısı, insanlara en çok faydalı olandır.'",
                    "18. Kaynak: Sahih-i Buhari, Edeb, 34: 'Güzel söz de bir sadakadır.'",
                    "19. Kaynak: Sahih-i Buhari, Rıkak, 3: 'Dünyada sanki bir garip veya yolcu gibi ol.'",
                    "20. Kaynak: Sünen-i Tirmizi, Daavat, 50: Sabah ve akşam zikirlerinin fazileti hakkında var olan sahih rivayetler."
                ],
                "sages": [
                    "1. Kaynak: İmam-ı Gazâlî, İhyâü Uvûmi'd-Din: Kâinat, Sani-i Zülcelal'in kudret kalemiyle yazılmış büyük bir kitaptır.",
                    "2. Kaynak: Mevlânâ Celâleddîn-i Rûmî, Mesnevi (Cilt 1): 'Testinin içinde ne varsa dışına o sızar.'",
                    "3. Kaynak: Muhyiddin İbn Arabî, Fusûsu'l-Hikem: Varlıkta tecelli eden her suret ilahi ilmin bir aynasıdır.",
                    "4. Kaynak: Yunus Emre, Divan: 'Yaratılanı hoş görürüz Yaratandan ötürü.'",
                    "5. Kaynak: Abdülkâdir Geylânî, Sırrü'l-Esrâr: Nefis aradan çekildiğinde faili hakiki muşahede edilir.",
                    "6. Kaynak: İmam-ı Rabbânî, Mektûbât (1. Cilt): Sebepleri vesile bilip hakiki müessirin Allah olduğunu idrak etmek tevhittir.",
                    "7. Kaynak: Şah-ı Nakşibend, Risale-i Kudsiye: 'Halvet der encümen' düsturu ile halk içinde Hak ile olmak.",
                    "8. Kaynak: İbrahim Hakkı Erzurumî, Marifetname: 'Hak şerleri hayreyler, zannetme ki gayreyler.'",
                    "9. Kaynak: Cüneyd-i Bağdâdî, Kuşeyri Risalesi: Tevhid, kulun beşeri sıfatlardan sıyrılıp Hak ile kaim olmasıdır.",
                    "10. Kaynak: Beyazıd-i Bistâmî, Tezkiretü'l-Evliya: Hakiki marifet, arayanın da arattıranın da O olduğunu bilmektir.",
                    "11. Kaynak: Hacı Bayrâm-ı Velî, Kaynaklarda geçen irfan düsturları: 'Kendini bilen Rabbini bilir.'",
                    "12. Kaynak: Aziz Mahmud Hüdâyî, Sohbetnâme: Kâinattaki her zerrenin zikri kalbe feyiz akıtır.",
                    "13. Kaynak: Niyâzî-i Mısrî, Divan-ı İlahiyat: 'Halk içinde bir ayinei mehrikes bakar bir an görür.'",
                    "14. Kaynak: Sadreddin Konevî, Miftâhü'l-Gayb: Zerre ile küre arasında ilahi nizam bakımından fark yoktur.",
                    "15. Kaynak: Bediüzzaman Said Nursî, Risale-i Nur Külliyâtı (Sözler - 33. Söz): Kâinat büyük bir mescit hükmündedir.",
                    "16. Kaynak: Eşrefoğlu Rûmî, Müzekki'n-Nüfûs: Sanatkârı tespih etmek kalbin cilasıdır.",
                    "17. Kaynak: Hasan-ı Basrî, Kelimat-ı Hikmet: İnsanın niyeti amelinden daha bereketlidir.",
                    "18. Kaynak: Fudayl bin İyâz, Tabakatü's-Sufiyye: İhlas, amellerin riyadan tamamen arındırılmasıdır.",
                    "19. Kaynak: Sehl et-Tüsterî, Tefsirü'l-Kur'an el-Azim: Kalbin huzuru, zikrin en yüksek derecesidir.",
                    "20. Kaynak: Ahmed er-Rifâî, İrşadü'l-Müslimîn: Aczini bilen kulun kâinata bakışı rahmet ve şefkat doludur."
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
                    "1. Kaynak: Sahih-i Müslim, Salat, 215: 'Kulun Rabbine en yakın olduğu an secde hâlidir.'",
                    "2. Kaynak: Sahih-i Müslim, Salat, 70: 'Kim bana bir defa salavat getirirse, Allah ona on rahmet ihsan eder.'",
                    "3. Kaynak: Sahih-i Buhari, Salat, 56: 'Yeryüzü bana mescit ve temiz kılındı.'",
                    "4. Kaynak: Sahih-i Müslim, Salat, 225: 'Allah için yapılan her secde bir derece yükseltir ve günahı siler.'",
                    "5. Kaynak: Sahih-i Müslim, Salat, 226: Hz. Rabia b. Ka'b'a Peygamberimizin secde konusunda tavsiyesi.",
                    "6. Kaynak: Sünen-i Tirmizi, Daavat, 4: 'Dilin sürekli Allah'ın zikriyle ıslak kalsın.'",
                    "7. Kaynak: Sahih-i Buhari, Deavat, 65: 'Mizanda ağır gelen iki hafif kelime...'",
                    "8. Kaynak: Sahih-i Müslim, Zikr, 38: Allah'ı zikreden meclisleri meleklerin kuşatması.",
                    "9. Kaynak: Sünen-i Ebu Davud, Salat, 207: 'Cuma günü bana salavatı artırın.'",
                    "10. Kaynak: Sünen-i Tirmizi, Vitir, 21: Kıyamet günü en yakın olanlar.",
                    "11. Kaynak: Ahmed bin Hanbel, Müsned: Katılımlı tespih rivayetleri.",
                    "12. Kaynak: Sünen-i Ebu Davud, Edeb, 97: Abdestli uyumanın fazileti.",
                    "13. Kaynak: Sahih-i Müslim, Zühd, 67: Yeryüzünde tevazu ile yürümek.",
                    "14. Kaynak: Sünen-i Tirmizi, Daavat, 129: Tespih ve tekbirin sevabı.",
                    "15. Kaynak: Sünen-i Ebu Davud, Edeb, 105: Tabiat olayları karşısında dua.",
                    "16. Kaynak: Sünen-i İbn Mace, Taharet, 48: Suyu tasarruflu kullanmak ve çevre.",
                    "17. Kaynak: Sahih-i Buhari, Edeb, 75: Secde azaplarının nefsaniyeti kırması.",
                    "18. Kaynak: Sahih-i Müslim, Müsafirin, 166: Gece ibadeti ve secde.",
                    "19. Kaynak: Beyhakî, Şuabü'l-İman: Müminin bakışı ve tefekkürü.",
                    "20. Kaynak: Taberani, Mu'cemü'l-Kebir: Tefekkürün ibadet değeri."
                ],
                "sages": [
                    "1. Kaynak: Mevlânâ Celâleddîn-i Rûmî, Fihi Ma Fih: Kümbet altında dönen her zerre aşkla döner.",
                    "2. Kaynak: Muhyiddin İbn Arabî, Futuhat-ı Mekkiyye: Kâinat secdegâhtır.",
                    "3. Kaynak: Yunus Emre, Risaletü'n-Nushiyye: Dağlar ve taşlar ile zikir.",
                    "4. Kaynak: İmam-ı Gazâlî, Kimyâ-yı Saâdet: Hakiki secde kalbin teslimiyetidir.",
                    "5. Kaynak: İbrahim Hakkı Erzurumî, Marifetname: Kâinat orkestrası ve şef irfanı.",
                    "6. Kaynak: Abdülkâdir Geylânî, Cilâü'l-Hâtır: Ruhun daima secdede kalması.",
                    "7. Kaynak: Cüneyd-i Bağdâdî, Lemaat: Zikirde fena bulmak.",
                    "8. Kaynak: Şems-i Tebrîzî, Makalat: Gölgeyi aradan çekmek.",
                    "9. Kaynak: Bediüzzaman Said Nursî, Mektubat (20. Mektup): Zerrattan yıldızlara tespihat.",
                    "10. Kaynak: Niyâzî-i Mısrî, Mektubat: İrfan ve zikir.",
                    "11. Kaynak: Hacı Bektaş-ı Velî, Makalat: Cemal ve kemal sırrı.",
                    "12. Kaynak: Aziz Mahmud Hüdâyî, Nefâisü'l-Mecâlis: Hava zermelerinin zikri.",
                    "13. Kaynak: Beyazıd-i Bistâmî, Risaleler: İbadette fena.",
                    "14. Kaynak: İmam-ı Rabbânî, Mektûbât: Sünnet ve salavatın nuru.",
                    "15. Kaynak: Eşrefoğlu Rûmî, Tarîkatnâme: Tabiatın tespihine ortak olmak.",
                    "16. Kaynak: Hallâc-ı Mansûr, Kitâbü't-Tavâsîn: Tevhid ve şuur.",
                    "17. Kaynak: Sadreddin Konevî, İ‘câzü’l-Beyân: Gölgelerin secdesi.",
                    "18. Kaynak: Ahmed Yesevî, Divan-ı Hikmet: Seher vakti zikri.",
                    "19. Kaynak: Ferîdüddîn Attâr, Mantıku't-Tayr: Varlığın tesbihi.",
                    "20. Kaynak: Ken'ân Rifâî, Sohbetler: Namazın ruhunu kâinata yaymak."
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
                    "1. Kaynak: Sahih-i Müslim, Selam, 47: 'Şüphesiz Allah güzeldir, güzelliği sever.'",
                    "2. Kaynak: Sahih-i Buhari, Marda, 1: Müminin her türlü zorluktan ders çıkararak terakki etmesi.",
                    "3. Kaynak: Sünen-i Tirmizi, İlim, 13: 'İlim öğrenmek her Müslümana farzdır.'",
                    "4. Kaynak: Ahmed bin Hanbel, Müsned: 'Nefsini bilen Rabbini bilir' hikmetli yaklaşımı.",
                    "5. Kaynak: Sahih-i Buhari, Bedu'l-Halk, 15: Karıncalara merhamet ve canlı hakları.",
                    "6. Kaynak: Sahih-i Tirmizi, Zühd, 57: İmtihanların derecesine göre olması.",
                    "7. Kaynak: Sahih-i Buhari, Rıkak, 1: 'İki nimet vardır ki insanların çoğu o hususta aldanmıştır: Sağlık ve boş vakit.'",
                    "8. Kaynak: Sünen-i İbn Mace, Zühd, 15: Uyku ve uyanıklıkta azaların şükrü.",
                    "9. Kaynak: Taberani, Mu'cemü'l-Kebir: Tefekkürün ehemmiyeti.",
                    "10. Kaynak: Sahih-i Müslim, Zühd, 59: Rızkın kefaleti ve tevekkül.",
                    "11. Kaynak: Sahih-i Buhari, Edeb, 27: 'Merhamet etmeyene merhamet olunmaz.'",
                    "12. Kaynak: Sahih-i Müslim, Zekat, 52: Vücuttaki her eklem için sadaka.",
                    "13. Kaynak: Sünen-i Tirmizi, Zühd, 59: Sabır ve şükür dengesi.",
                    "14. Kaynak: Sahih-i Buhari, Tıb, 1: 'Allah bir dert indirdiyse mutlaka şifasını da indirmiştir.'",
                    "15. Kaynak: Sünen-i Tirmizi, Sıfatü'l-Kıyamet, 25: Akıllı kişinin nefsini hesaba çekmesi.",
                    "16. Kaynak: Müsned-i Şihab: Günlerin kıymeti.",
                    "17. Kaynak: Sünen-i İbn Mace, Zühd, 22: Haset ve kanaat.",
                    "18. Kaynak: Sahih-i Buhari, Tevhid, 34: Her varlığın yaratılış gayesine kolaylaştırılması.",
                    "19. Kaynak: Beyhakî, Şuabü'l-İman: Arı misali faydalı olmak.",
                    "20. Kaynak: Sahih-i Müslim, Tevbe, 14: Rahmetin gazabı geçmesi."
                ],
                "sages": [
                    "1. Kaynak: Bediüzzaman Said Nursî, Sözler (33. Söz - Ehadiyet Risalesi): Bir çiçeği yaratamayan güneşi de yaratamaz.",
                    "2. Kaynak: Mevlânâ Celâleddîn-i Rûmî, Mesnevi: Zıtlıkların hikmeti ve âlemin nizamı.",
                    "3. Kaynak: İmam-ı Gazâlî, İhyâ: Beden mimarisi ve uyku mucizesi.",
                    "4. Kaynak: Muhyiddin İbn Arabî, Füsûs: Şer ve kusur görünenlerin tablodaki renk uyumu.",
                    "5. Kaynak: İbrahim Hakkı Erzurumî, Marifetname: Zerrattan küreye hikmetler.",
                    "6. Kaynak: Şah-ı Nakşibend, Nasihatler: İmtihanda rıza göstermek.",
                    "7. Kaynak: Yunus Emre, Divan: Kudretin tecellisi.",
                    "8. Kaynak: Abdülkâdir Geylânî, Gunyetü't-Talibîn: Sıkıntıların hikmeti.",
                    "9. Kaynak: İmam-ı Rabbânî, Mektûbât: Memur olan varlıklar.",
                    "10. Kaynak: Sadreddin Konevî, Miftâhü'l-Gayb: Ehadiyet mührünün sırrı.",
                    "11. Kaynak: Cüneyd-i Bağdâdî, Risaleler: Verilmeyen nimetin hikmeti.",
                    "12. Kaynak: Hacı Bayrâm-ı Velî, Menakıb: İnsan meyvesi.",
                    "13. Kaynak: Beyazıd-i Bistâmî: İmtihandaki gizli lütuflar.",
                    "14. Kaynak: Niyâzî-i Mısrî, Divan: Üç boyutlu suret perdesi.",
                    "15. Kaynak: Eşrefoğlu Rûmî, Müzekki'n-Nüfûs: Gafletten uyanış.",
                    "16. Kaynak: Aziz Mahmud Hüdâyî, Vâkıfat: Vazifesini yapan zerrat.",
                    "17. Kaynak: Ferîdüddîn Attâr, Tezkiretü'l-Evliya: Karıncanın azmi.",
                    "18. Kaynak: Hasan-ı Basrî, Zühd: Ömür sermayesi.",
                    "19. Kaynak: Sehl et-Tüsterî, Tefsir: Nimetin hakiki şükrü.",
                    "20. Kaynak: Ken'ân Rifâî, Sohbetler: Çile ve terakki."
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
                    "1. Source: Sahih al-Bukhari 1, Sahih Muslim 1907: 'Actions are judged by intentions...'",
                    "2. Source: Sahih Muslim 1631: 'When a human dies, their deeds cease except for three...'",
                    "3. Source: Sahih Muslim 1893: 'Whoever guides to a good has a reward like its doer.'",
                    "4. Source: Sahih al-Bukhari 47, Sahih Muslim 8: Hadith of Gabriel on Ihsan.",
                    "5. Source: Sahih Muslim 2999: 'Wondrous is the affair of the believer...'",
                    "6. Source: Sunan an-Nasa'i 324: 'Whoever does not thank people has not thanked Allah.'",
                    "7. Source: Sahih Muslim 2564: 'Indeed Allah does not look at your bodies or forms, but at your hearts.'",
                    "8. Source: Sahih Muslim 54: 'You will not enter Paradise until you believe...'",
                    "9. Source: Jami' at-Tirmidhi 1956: 'Your smile for your brother is charity.'",
                    "10. Source: Sahih al-Bukhari 438, Sahih Muslim 521: 'The earth has been made for me a mosque and pure.'",
                    "11. Source: Sahih Muslim 482: 'The closest a servant is to his Lord is when he is prostrating.'",
                    "12. Source: Jami' at-Tirmidhi 3383: Best remembrance and gratitude.",
                    "13. Source: Sahih al-Bukhari 6407: The example of one who remembers Allah.",
                    "14. Source: Sahih Muslim 91: 'No one with an atom of pride will enter Paradise.'",
                    "15. Source: Sahih Muslim 2588: Humility elevates one before Allah.",
                    "16. Source: Sahih al-Bukhari 69, Sahih Muslim 1734: 'Facilitate and do not make difficult.'",
                    "17. Source: Al-Mu'jam al-Awsat 5787: 'The best of people are those most beneficial to others.'",
                    "18. Source: Sahih al-Bukhari 6023: 'A good word is charity.'",
                    "19. Source: Sahih al-Bukhari 6416: 'Be in this world as if you were a stranger or a traveler.'",
                    "20. Source: Jami' at-Tirmidhi 3391: Rewards of morning and evening remembrance."
                ],
                "sages": [
                    "1. Source: Al-Ghazali, Ihya Ulum al-Din: The universe is a grand book written by Divine Power.",
                    "2. Source: Rumi, Masnavi (Vol. 1): 'Whatever is in the pitcher spills out.'",
                    "3. Source: Ibn Arabi, Fusus al-Hikam: Every form is a mirror of divine knowledge.",
                    "4. Source: Yunus Emre, Divan: 'We love the created for the Creator's sake.'",
                    "5. Source: Abdul-Qadir Gilani, Sirr al-Asrar: When ego fades, the True Doer is witnessed.",
                    "6. Source: Imam Rabbani, Maktubat (Vol. 1): Seeing causes as veils and God as the Causer.",
                    "7. Source: Baha'ud-Din Naqshband, Risala-i Qudsiyya: Solitude in the crowd ('Halvet der encümen').",
                    "8. Source: Ibrahim Hakki Erzurumi, Marifetname: Divine turning of hardships into ease.",
                    "9. Source: Junayd of Baghdad, Al-Risala al-Qushayriyya: Tawhid and annihilation of self.",
                    "10. Source: Bayazid Bastami, Tadhkirat al-Awliya: The Seeker and Sought are His grace.",
                    "11. Source: Haci Bayram Veli: 'He who knows himself knows his Lord.'",
                    "12. Source: Aziz Mahmud Hudayi, Sohbetname: The remembrance of atoms.",
                    "13. Source: Niyazi Misri, Divan: Creation as a mirror.",
                    "14. Source: Sadr al-Din al-Qunawi, Miftah al-Ghayb: Harmony of atom and sphere.",
                    "15. Source: Said Nursi, Risale-i Nur (The Words - 33rd Word): The universe as a vast mosque.",
                    "16. Source: Esrefoglu Rumi, Muzekki al-Nufus: Polishing the heart through praise.",
                    "17. Source: Hasan al-Basri, Hikmah sayings: Intention surpasses action in blessing.",
                    "18. Source: Fudayl ibn Iyad, Tabaqat al-Sufiyya: Sincerity (Ihlas).",
                    "19. Source: Sahl al-Tustari, Tafsir: Heartfelt presence as supreme remembrance.",
                    "20. Source: Ahmed al-Rifa'i, Irshad al-Muslimin: Compassion born of recognizing human weakness."
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
                    "1. Source: Sahih Muslim 482: 'The closest a servant is to his Lord is when he is prostrating.'",
                    "2. Source: Sahih Muslim 408: 'Whoever sends blessings upon me once, Allah sends ten upon him.'",
                    "3. Source: Sahih al-Bukhari 438, Sahih Muslim 521: The earth made pure and a mosque.",
                    "4. Source: Sahih Muslim 225: Prostration raises one in rank.",
                    "5. Source: Sahih Muslim 489: Advice to Rabi'ah b. Ka'b.",
                    "6. Source: Jami' at-Tirmidhi 3375: Keeping the tongue moist with remembrance.",
                    "7. Source: Sahih al-Bukhari 6406: Two light phrases heavy on the scale.",
                    "8. Source: Sahih Muslim 2699: Gathering for remembrance and angels.",
                    "9. Source: Sunan Abu Dawud 1047: Increasing Salawat on Fridays.",
                    "10. Source: Jami' at-Tirmidhi 484: Those closest on Judgment Day.",
                    "11. Source: Musnad Ahmad: Echoing praise.",
                    "12. Source: Sunan Abu Dawud 5051: Purity before sleep.",
                    "13. Source: Sahih Muslim 2165: Walking with humility.",
                    "14. Source: Jami' at-Tirmidhi 3598: Weight of glorification.",
                    "15. Source: Sunan Abu Dawud 1090: Prayers during natural phenomena.",
                    "16. Source: Sunan Ibn Majah 425: Water conservation.",
                    "17. Source: Sahih al-Bukhari 807: Dissolving ego through prostration.",
                    "18. Source: Sahih Muslim 758: Night prayer.",
                    "19. Source: Shu'ab al-Iman: Believer's contemplation.",
                    "20. Source: Al-Mu'jam al-Kabir: Value of contemplation."
                ],
                "sages": [
                    "1. Source: Rumi, Fihi Ma Fih: Every spinning atom dances in love.",
                    "2. Source: Ibn Arabi, Futuhat al-Makkiyya: The cosmos as a sanctuary.",
                    "3. Source: Yunus Emre, Risalat al-Nushiyya: Calling upon the Lord with nature.",
                    "4. Source: Al-Ghazali, Kimiya-i Sa'adat: True prostration of the heart.",
                    "5. Source: Ibrahim Hakki Erzurumi, Marifetname: Cosmic orchestra.",
                    "6. Source: Abdul-Qadir Gilani, Jila al-Khatir: Eternal prostration of the soul.",
                    "7. Source: Junayd of Baghdad: Annihilation in remembrance.",
                    "8. Source: Shams Tabrizi, Makalat: Moving the shadow aside.",
                    "9. Source: Said Nursi, Letters (20th Letter): Praise from atoms to stars.",
                    "10. Source: Niyazi Misri, Maktubat: Gnosis and remembrance.",
                    "11. Source: Haci Bektas Veli, Makalat: Beauty and perfection.",
                    "12. Source: Aziz Mahmud Hudayi, Nafais al-Majalis: Air particle remembrance.",
                    "13. Source: Bayazid Bastami: Worship from His grace.",
                    "14. Source: Imam Rabbani, Maktubat: Light of prophetic adherence.",
                    "15. Source: Esrefoglu Rumi, Tarikatname: Joining natural praise.",
                    "16. Source: Mansur al-Hallaj, Kitab al-Tawasin: Unity and awareness.",
                    "17. Source: Sadr al-Din al-Qunawi: Prostration of shadows.",
                    "18. Source: Ahmad Yasawi, Divan-i Hikmet: Dawn remembrance.",
                    "19. Source: Farid al-Din Attar, Mantiq al-Tayr: Praise of creation.",
                    "20. Source: Ken'an Rifai, Sohbetler: Carrying prayer into the world."
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
                    "1. Source: Sahih Muslim 147: 'Indeed Allah is Beautiful and loves beauty.'",
                    "2. Source: Sahih al-Bukhari 5641: Believers learning and growing from trials.",
                    "3. Source: Sunan Ibn Majah 224: 'Seeking knowledge is an obligation upon every Muslim.'",
                    "4. Source: Al-Maqasid al-Hasana: 'He who knows himself knows his Lord.'",
                    "5. Source: Sahih al-Bukhari 3319: Prohibition of harming ants and animals.",
                    "6. Source: Jami' at-Tirmidhi 2398: Trials proportional to faith.",
                    "7. Source: Sahih al-Bukhari 6412: Two blessings squandered: health and free time.",
                    "8. Source: Sunan Ibn Majah 1385: Gratitude for sleep and waking.",
                    "9. Source: Al-Mu'jam al-Awsat: Value of an hour of contemplation.",
                    "10. Source: Jami' at-Tirmidhi 2344: Reliance on Allah and sustenance.",
                    "11. Source: Sahih al-Bukhari 6013: 'He who does not show mercy will not be shown mercy.'",
                    "12. Source: Sahih Muslim 720: Daily charity for every joint.",
                    "13. Source: Jami' at-Tirmidhi 2400: Patience and gratitude.",
                    "14. Source: Sahih al-Bukhari 5678: Every disease has a cure.",
                    "15. Source: Jami' at-Tirmidhi 2459: The smart person holds himself accountable.",
                    "16. Source: Al-Shihab: Value of each new day.",
                    "17. Source: Jami' at-Tirmidhi 2465: Contentment versus envy.",
                    "18. Source: Sahih al-Bukhari 4940: Every creature facilitated for its purpose.",
                    "19. Source: Shu'ab al-Iman: Being like the honeybee.",
                    "20. Source: Sahih Muslim 2751: Divine mercy exceeding wrath."
                ],
                "sages": [
                    "1. Source: Said Nursi, The Words (33rd Word): The Seal of Oneness in atoms and flowers.",
                    "2. Source: Rumi, Masnavi: Wisdom of opposites.",
                    "3. Source: Al-Ghazali, Ihya: Human biology and sleep miracles.",
                    "4. Source: Ibn Arabi, Fusus: Flaws as dark pigments in a masterpiece.",
                    "5. Source: Ibrahim Hakki Erzurumi, Marifetname: Macrocosm in an atom.",
                    "6. Source: Baha'ud-Din Naqshband: Acceptance in trials.",
                    "7. Source: Yunus Emre, Divan: True power belongs to the Creator.",
                    "8. Source: Abdul-Qadir Gilani, Gunyat al-Talibin: Hardships as honored guests.",
                    "9. Source: Imam Rabbani, Maktubat: All entities as obedient servants.",
                    "10. Source: Sadr al-Din al-Qunawi: The manifestation of Oneness.",
                    "11. Source: Junayd of Baghdad: Wisdom in withholding.",
                    "12. Source: Haci Bayram Veli: Humanity as the cosmic fruit.",
                    "13. Source: Bayazid Bastami: Mercy hidden within trials.",
                    "14. Source: Niyazi Misri, Divan: The three-dimensional veil.",
                    "15. Source: Esrefoglu Rumi, Muzekki al-Nufus: Awakening from heedlessness.",
                    "16. Source: Aziz Mahmud Hudayi: Atoms fulfilling duties.",
                    "17. Source: Farid al-Din Attar: Discipline of the ant.",
                    "18. Source: Hasan al-Basri: Life as passing days.",
                    "19. Source: Sahl al-Tustari, Tafsir: True gratitude for blessings.",
                    "20. Source: Ken'an Rifai, Sohbetler: Purification through the crucible of fire."
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
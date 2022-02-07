<br />
<p align="center">
  <a href="https://github.com/samet-g/tornado">
    <img src="images/twister.png" alt="Logo" width="80" height="80">
  </a>

  <h3 align="center">Anonymously Reverse shell over Tor Network using Hidden Services without portfortwarding</h3>

  <p align="center">
    Tor ağı ile Dark Web servislerini kullanarak anonim biçimde port yönlendirmeden ters bağlantı     
    <br />
    <a href="https://github.com/samet-g/tornado"><strong>Explore the docs » Projeyi keşfet</strong></a>
    <br />
    <a href="https://www.gnu.org/licenses/gpl-3.0.en.html"></a>
      <img src="https://img.shields.io/badge/license-GPL3-_red.svg"></a>
  </p>
</p>

<details open="open">
  <summary>Table of Contents / İçerik Bölümü</summary>
  <ol>
    <li>
      <a href="#about-the-project--proje-hakkında">About the Project / Proje Hakkında</a>
      <ul>
        <li><a href="#built-with--kullanılanlar">Built With / Kullanılanlar</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started--başlangıç">Getting Started / Başlangıç</a>
      <ul>
        <li><a href="#installation--kurulum">Installation / Kurulum</a></li>
      </ul>
    </li>
    <li><a href="#usage--kullanım">Usage / Kullanım</a></li>  
    <li><a href="#roadmap--yol-haritası">Roadmap / Yol Haritası</a></li>
    <li><a href="#contributing--katkı">Contributing / Katkı</a></li>
    <li><a href="#license--lisans">License / Lisans</a></li>
    <li><a href="#disclaimer--sorumluluk">Disclaimer / Sorumluluk</a></li>
  </ol>
</details>

> If you are having any os compatiblity issue, let me know. I will try to fix as soon as possible so let's explore the docs.

> Herhangi bir işletim sistemi uyumsuzluğu varsa, bana bildirin. En kısa sürede düzeltmeye çalışacağım, hadi dökümanı inceleyelim.

## About the Project / Proje Hakkında
Currently this project have that features.

    Create a hidden service                                   |   Dark web servisi oluşturma
    Generate msfvenom payload with fully undetectable         |   Yakalanmayan msfvenom arka kapısı oluşturma
    Hidden service becomes available outside tor network      |   Dark web servisini tor ağının dışına çıkarma


[![asciicast](https://asciinema.org/a/467317.svg)](https://asciinema.org/a/467317)

This project, implements tor network with metasploit-framework tool and msfvenom module. You can easily create hidden services for your LHOST .onion domain without portforwarding. If you have experience different remote administration tools, probably you know you need forward port with VPN or NGROK but in this sense, the Tor network offers the possibility of making services in a machine accessible as hidden services without portforwarding, by taking advantage of the anonymity it offers and thereby preventing the real location of the machine from being exposed.  

Bu proje, tor ağı ile birlikte metasploit-framework aracının msfvenom modülünü uygular. Kolayca port yönlendirme yapmadan LHOST için .onion dark web servisi oluşturabilirsiniz. Farklı uzaktan bağlantı araçları deneyiminiz varsa, büyük ihtimalle VPN kullanarak veya NGROK kullanarak port yönlendirme yapmanız gerektiğini biliyorsunuz ama bu proje ile tor ağının sunduğu anonimlikten yararlanarak port yönlendirmeden gizli servisteki hizmetlere erişme imkanı sunar böylece makinenin gerçek konumun açığa çıkmasını engeller.

### Built With / Kullanılanlar

* [Tor](https://www.torproject.org)
* [Metasploit](https://www.metasploit.com/)
* [Tor2Web](https://www.tor2web.org/)


## Getting Started / Başlangıç

To get a local copy up and running follow these simple steps.  

Kendi bilgisayarınızda çalıştırmak için bu basit adımları izleyin.

### Installation / Kurulum

1. Clone the repo | Projeyi indir.
   ```bash
   git clone https://github.com/samet-g/tornado.git
   ```
2. Install Python packages | Gerekli Python paketlerini yükle.
   ```bash
   pip3 install -r requirements.txt
   ```

## Usage / Kullanım

* Run with Python as Administrator 
*   Yönetici olarak çalıştır
   ```bash
   python3 tornado.py
   ```

## Roadmap / Yol Haritası

See the [open issues](https://github.com/samet-g/tornado/issues) for a list of proposed features  
Listener should be integrity to Windows.  

Sorunlar için [açık sorunları](https://github.com/samet-g/tornado/issues) kontrol edin.  
Windows ile entegre listener olsa iyi olur.

## Contributing / Katkı

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated** especially <a href="#roadmap--yol-haritası">Roadmap / Yol Haritası</a> check this to-do list.  

Katkılar, açık kaynak topluluğu için büyük nimettir özellikle <a href="#roadmap--yol-haritası">Roadmap / Yol Haritası</a> kısmındaki yapılacak-listesini kontrol edin.  

1. Fork the Project | Projeyi forkla.
2. Create your Feature Branch | Katkıda Bulun  
`git checkout -b feature/YeniOzellik`
3. Commit your Changes | Değişiklikleri Commitle  
`git commit -m 'Add some YeniOzellik'`
4. Push to the Branch | Değişikliğini Yolla  
`git push origin feature/YeniOzellik`
5. Open a Pull Request | Pull Request Aç

## License / Lisans

Distributed under the GNU License.  
See `LICENSE` for more information.

GNU Lisansı altında dağıtılmaktadır.  
Daha fazla bilgi için `LICENSE` bölümüne bakın.

## Disclaimer / Sorumluluk

This tool is only for testing and can only be used where strict consent has been given. Do not use it for illegal purposes! It is the end user’s responsibility to obey all applicable local, state and federal laws. I assume no liability and are not responsible for any misuse or damage caused by this tool and software.

Bu proje sadece test etmek içindir ve yalnızca kesin onayın verildiği durumlarda kullanılabilir. Yasadışı amaçlar için kullanmayın! Geçerli tüm yerel, eyalet ve federal yasalara uymak son kullanıcının sorumluluğundadır. Ben bu projenin ve yazılımın neden olduğu herhangi bir yanlış kullanım veya hasardan sorumlu değilim.
<!---/samogod/samet-g/-->
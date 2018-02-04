# VCI-crawler

## Hướng dẫn cài đặt

### B1: Cài đặt môi trường và run server

    $ pip install -r requirements.txt
    $ python manage.py runserver
    
### B2: Tải data

Tải data [tại đây](https://drive.google.com/open?id=142RgTCFkE44kRDcQnOHsTUJmlhy8r77P), sau đó đặt vào thư mục gốc của project (pycrawler/data)

### B3: Chạy code

Vào localhost:8000, vào mục 2017 lần lượt bấm vào 2 menu item Scopus 2017 và ISI 2017. 

Sau khi bấm 1 item sẽ phải đợi 1 lúc, khi xong sẽ tự redirect lại home.

Sau khi xong 2 menu item trên thì bấm vào "Author to json" và "ISI author json" nếu cần field author_json.
 
## Cấu trúc file data và db:

data Scopus có dạng 2017_xxxx_yyyy.csv với xxxx là tên viết tắt của subject, yyyy là số bài trong subject. Tổng yyyy sẽ bằng đúng số record khi search trên scopus của năm 2017.

data Isi có dạng 2017_xxxx_yyyy.bib với xxxx và yyyy là start và end của đoạn record. Số lượng record khi search sẽ chia thành các đoạn độ dài tối đa 500 bản ghi. Trong bảng isi_documents_2017 có cột start và end chỉ đoạn record của nó.  


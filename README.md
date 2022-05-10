# Rick-and-Morty-API-Python
მოცემული პროგრამა უკავშირდება Rick&Morty API-ს, შედეგად კი პირველ რიგში გვიბეჭდავს ზუსტ დროს(GMT ფორმატში), თუ როდის მიიღო პროგრამამ გამოხმაურება api-ის სერვერიდან, სერვერის სახელსა და status code-ს.
შემდეგ მოაქვს ინფორმაცია ყველა Morty-ზე რომელთა სტატუსიც არის Dead(გარდაცვლილი) და ათავსებს json ფაილში.
მოაქვს ინფორმაცია ყველა პერსონაჟის შესახებ(სულ 826),(პერსონაჟების სახელები, სქესი, "საცხოვრებელი" ლოკაცია)თავსდება sql ცხრილში.
შემდეგ ამავე api-დან მოაქვს ინფორმაცია ლოკაციების შესახებ ინფორმაციის წამოღება და თავსდება მისთვის განკუთვნილ  sql ცხრილში.
ბოლოს კი  გამოითვლება თუ რამდენი ლოკაციაა გაერთიანებული თითოეულ განზომილებაში("dimension") 
და ახლად შექმნილ განზომილებების ცხრილში თავსდება შესაბამისი მონაცემები (განზომილების სახელი და გაერთიანებული ლოკაციების რაოდენობა)

p.s პროგრამის გაშვებას სჭირდება დაახლოებით 5-7 წუთი (ვერ მოხერხდა ოპტიმიზაცია), რადგან 1000-მდე request-ის გაგზავნა უწევს.
თუ მისი გაშვება თქვენთვის არაკომფორტული იქნება შეგიძლიათ ამავე repository-ში განთავსებული sqlite ფაილები ჩამოტვირთოთ, გახსნათ შესაბამისი პროგრამების გამოყენებით
და იხილოთ პროგრამის მიერ შექმნილი ცხრილები.

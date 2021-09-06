import json
records = {
            101 : {"name" : "KitKat"                    , "price" : 30 , "stock" : 50 , 'category' : 'Cadbury' , 'company' : 'Nestle Global'},
            102 : {"name" : "MiklyBar"                  , "price" : 20 , "stock" : 45 , 'category' : 'Cadbury' , 'company' : 'Nestle'},
            103 : {"name" : "Amul Chocolate"            , "price" : 70 , "stock" : 20 , 'category' : 'Cadbury' , 'company' : ' Amul'},
            104 : {"name" : "Ferrero Rocher Chocolate"  , "price" : 150 , "stock" : 10 , 'category' : 'Cadbury' , 'company' : 'Ferrero'},
            105 : {"name" : "Kinder Joy"                , "price" : 40 , "stock" : 40 , 'category' : 'Candy' , 'company' : 'Ferrero'},
            106 : {"name" : "Dairy Milk"                , "price" : 10 , "stock" : 200 , 'category' : 'Cadbury' , 'company' : 'Cadbury'},
            107 : {"name" : "5 star"                    , "price" : 5 , "stock" : 120 , 'category' : 'Cadbury' , 'company' : 'Cadburys'},
            108 : {"name" : "Fuse"                      , "price" : 35 , "stock" : 35 , 'category' : 'Cadbury' , 'company' : 'Mondelez India'},
            109 : {"name" : "Munch"                     , "price" : 10 , "stock" : 40 , 'category' : 'Cadbury' , 'company' : 'Nestle'},
            110 : {"name" : "Perk"                      , "price" : 10 , "stock" : 40 , 'category' : 'Cadbury' , 'company' : 'Mondelez India'},
            111 : {"name" : "Snickers"                  , "price" : 25 , "stock" : 45 , 'category' : 'Candy Bar' , 'company' : 'Mars'},
            112 : {"name" : "Hind & Seek Biscuits"      , "price" : 20 , "stock" : 70 , 'category' : 'Biscuit' , 'company' : 'Parle'},
            113 : {"name" : "20-20 Cookies Biscuits"    , "price" : 5  , "stock" : 80 , 'category' : 'snack' , 'company' : 'Parle G'},
            114 : {"name" : "Bourbon Biscuits"          , "price" : 10 , "stock" : 150 , 'category' : 'Biscuit' , 'company' : 'Britania'},
            115 : {"name" : "Choco pie"                 , "price" : 50  , "stock" : 50 , 'category' : 'Cadbury' , 'company' : 'Orion'},
            116 : {"name" : "Brookside chocolate"       , "price" : 50  , "stock" : 100 , 'category' : 'Dark Chocolate' , 'company' : 'Hershey'},
            117 : {"name" : "Friberg Chocolate"         , "price" : 150  , "stock" : 10 , 'category' : 'Dark Chocolate' , 'company' : 'Parle Products'},
            118 : {"name" : "Good Day Cookies"          , "price" : 35  , "stock" : 25 , 'category' : 'Cookies' , 'company' : 'Britania'},
            119 : {"name" : "Frech Fries"               , "price" : 150  , "stock" : 60 , 'category' : 'snack' , 'company' : 'McCain Foods Limited'},
            120 : {"name" : "Kurkure"                   , "price" : 5  , "stock" : 150 , 'category' : 'snack' , 'company' : 'Balaji'},
            121 : {"name" : "Wafers"                    , "price" : 5  , "stock" : 200 , 'category' : 'snack' , 'company' : 'Balaji'},
            122 : {"name" : "Doritos"                   , "price" : 10  , "stock" : 100 , 'category' : 'snack' , 'company' : 'PepsiCo'},
            123 : {"name" : "Mad Angles"                , "price" : 10  , "stock" : 100 , 'category' : 'snack' , 'company' : 'Mad Angles'},
            124 : {"name" : "Lays"                      , "price" : 15  , "stock" : 150 , 'category' : 'snack' , 'company' : 'PepsiCo'},
            125 : {"name" : "Cheetos"                   , "price" : 10  , "stock" : 170 , 'category' : 'snack', 'company' : 'Frito-Lay'},
            126 : {"name" : "Pepsi"                     , "price" : 30  , "stock" : 140 , 'category' : 'Drink', 'company' : 'PepsiCo'},
            127 : {"name" : "Popeyes Biscuits "         , "price" : 60  , "stock" : 35 , 'category' : 'Biscuit' , 'company' : ''},
            128 : {"name" : "Coca-Cola"                 , "price" : 40  , "stock" : 100 , 'category' : 'Drink' , 'company' : 'Coca Cola'},
            129 : {"name" : "Appy Fizz"                 , "price" : 15  , "stock" : 140 , 'category' : 'Drink' , 'company' : 'Parle Agro'},
            130 : {"name" : "Thums Up"                  , "price" : 40  , "stock" : 250 , 'category' : 'Drink' , 'company' : 'Coca Cola'},
            
         }

js = json.dumps(records)#dict
fd = open("records.json",'w')
fd.write(js)
fd.close()

fd = open("records.json",'r')
txt = fd.read()
fd.close()
records = json.loads(txt)#dict

print("\n********WEL-COME********\n")
ch='y'
while ch == 'y':
    try:
        ch = int(input("1. Purchase\n2. Add Products\n3. Delete\n4. Exit\nEnter Choice : "))
    except ValueError:
        print("\n-----Invalid choice-----")
        continue
    else:
        if ch == 1:
            ans = 'y'
            while ans == 'y' :
                pid = input("\nEnter Product Id : ")
                if pid in records :
                    m = 'y'
                    while m == 'y':
                        if records[pid]['stock'] == 0:
                            print("\n******STOCK OVER******")
                            break
                        quantity = int(input("Enter Product Quantity : " ))
                        if records[pid]['stock'] >= quantity:
                            print("\nProduct Name: ",records[pid]['name'])
                            print("Total Stock Left: ",records[pid]['stock']-quantity)
                            print("\nPurchase details : ")
                            print("Name of Product : ",records[pid]['name'])
                            print("Quantity Ordered : ",quantity)
                            print("Price per unit: ",records[pid]['price'])
                            print("-----------------------")
                            print("Total : ",records[pid]['price']*quantity)
                            qn = records[pid]['stock']-quantity
                            
                            records[pid] = {'name' : records[pid]['name'] , 'price' : records[pid]['price'] , 'stock' : qn, 'category' : records[pid]['category'] , 'company' : records[pid]['company']}
                            
                            js = json.dumps(records)
                            s = open("records.json",'w')
                            s.write(js)
                            s.close()
                            
                            pr = records[pid]['price']*quantity
                            
                            record= {'product id' : pid , 'name' : records[pid]['name'] , 'price' : pr , 'stock' : qn, 'category' : records[pid]['category'] , 'company' : records[pid]['company']}
                            js1=json.dumps(record)
                            s1 = open("Sales.json",'a')
                            s1.write(js1)
                            s1.write("\n")
                            s1.close()
                            break
                        elif records[pid]['stock'] < quantity and records[pid]['stock'] != 0 :
                            print("Only ",records[pid]['stock'],records[pid]['name']," Left......")  
                        m = input("\nWant To Buy Less? y|n : ")
                else:
                        print("\n.....Sorry!Product Not Found.....\n ")
                ans = input("\nWanna Continue Purchasing? y|n : ")
            ch = input('Wanna Continue with IMS? y|n : ') 
        elif ch == 2 :
            ans = 'y'
            while ans == 'y':
                prod_id = input("Enter product id : " )
                name = input("Enter product name : ")
                pr = int(input("Enter product price : "))
                qn = int(input("Enter Quantity : "))
                cr = input("Enter category : ")
                comp = input("Enter Company : ")
                records[prod_id] = {'name' : name, 'price' : pr , 'stock' : qn, 'category' : cr , 'company' : comp}

                js = json.dumps(records)
                
                fd = open("records.json",'w')
                fd.write(js)
                fd.close()
                print("********Record Inserted successfully********")
                ans = input("Wanna Insert More Products? y|n : ")
            ch=input("Want to continue with IMS? y|n : ")

        elif ch == 3:
            ans = 'y'
            fd = open("records.json",'r')
            txt = fd.read()
            fd.close()
            records = json.loads(txt)
            while ans == 'y':
                pid = input("Enter product id to delete item : ")
                if pid in records:
                    del records[pid]
                    fd = open("records.json",'w')
                    fd.write(js)
                    fd.close()
                    print("********Item Deleted********")
                    
                else:
                    print("No item Exists")   
                ans=input("Want to continue? y|n : ")
            ch=input("Want to continue with IMS? y|n : ")
        elif ch == 4:
            exit
        else :
            print("-----Invalid choice-----")
            ch = input("Want To Continue with IMS? y|n : ")


import jaydebeapi
import time

# time function for own use


def time_it(func):
    def inner():
        start = time.time()
        func()
        end = time.time()
        print('Time used :{}sec'.format(end-start))
    return inner

@time_it
def func1():
    db_path2 = "res/accdb/northwind.accdb"
    psw = "12345678"
    usr="user"

    db_path_final2=f"jdbc:ucanaccess://{db_path2};jackcessOpener=com.robinmakkaiching.ucanaccess.crypto.CryptCodecOpener"
    driver="net.ucanaccess.jdbc.UcanaccessDriver"
    ucanaccess_jars = [
        "res/lib/UCanAccess-5.0.1.bin/ucanaccess-5.0.1.jar",
        "res/lib/UCanAccess-5.0.1.bin/lib/commons-lang3-3.8.1.jar",
        "res/lib/UCanAccess-5.0.1.bin/lib/commons-logging-1.2.jar",
        "res/lib/UCanAccess-5.0.1.bin/lib/hsqldb-2.5.0.jar",
        "res/lib/Jackcess-4.0/jackcess-4.0.0.jar",
        "res/lib/Jackcess-4.0/jackcess-encrypt-4.0.1.jar",
        "res/lib/Jackcess-4.0/CryptCodecOpener.jar",
        "res/lib/bouncycastle/bin/bcprov-jdk15on-160.jar",
        ]
    # Unix use":" as seperator , in windows use ";" as seperator of classpaths
    mylibpath = ";".join(ucanaccess_jars)
    conn = jaydebeapi.connect(jclassname=driver, url=db_path_final2, driver_args=[usr, psw], jars=mylibpath)
    cur = conn.cursor()
    cur.execute("SELECT TOP 20 Products.[Product Name], [Order Details].* FROM Products INNER JOIN [Order Details] ON Products.ID = [Order Details].[Product ID]")
    result = cur.fetchall()
    #print(type(result))  #Result in "list"
    mycounter=1
    for i in result:
        print(mycounter," Data：", i)
        mycounter += 1

    conn.close()
    del mycounter,ucanaccess_jars,db_path2,psw,usr,db_path_final2,driver,mylibpath,conn,cur,result



if __name__ == '__main__':

    func1()
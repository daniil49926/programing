#include <iostream>
#include <Windows.h>

#include "mysqlheaders/mysqlheaders/mysql.h"
#include "mysqlheaders/mysqlheaders/mysql_com.h"
#include "mysqlheaders/mysqlheaders/mysql_version.h"
#include "mysqlheaders/mysqlheaders/my_alloc.h"


using namespace std;


int main() {
    setlocale(LC_ALL, "ru");
    MYSQL* conn;
    MYSQL_ROW row;
    MYSQL_RES* res;
    conn = mysql_init(0);
    conn = mysql_real_connect(conn, "###", "###", "###", "###", 0, NULL, 0);
    string result = "";

    int qstate = 0;


    if (conn) {
        int qstate2 = mysql_query(conn, "SET NAMES cp1251");
        int qstate = mysql_query(conn, "SELECT * FROM order_in_shop");

        if (!qstate) {
            res = mysql_store_result(conn);

            while (row = mysql_fetch_row(res)) {
                cout << row[0] << " | " << row[1] << " | " << row[2] << " | " << row[3] << " | " << row[4] << endl;
                result += row[0], row[1], row[2], row[3], row[4], "\n";
            }
        }
    }
}

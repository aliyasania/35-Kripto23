/*
Nama        : Aliya Sania
NPM         : 140810210035
Kelas       : A
Deskripsi    : Tugas 2 Program Enkripsi Dekripsi dengan Shift Cipher
*/

#include <iostream>
using namespace std;

string enkripsi(int key, char str[])
{
    char temp;  
    for (int i = 0; str[i] != '\0'; i++)
    {
        temp = str[i];
        if (temp >= 'a' && temp <= 'z')
        {
            temp = temp + key;  
            if (temp > 'z')
            {
                temp = temp - 'z' + 'a' - 1;    
            }
            str[i] = temp;  
        }
        else if (temp >= 'A' && temp <= 'Z')   
        {
            temp = temp + key;
            if (temp > 'Z')
            {
                temp = temp - 'Z' + 'A' - 1;
            }
            str[i] = temp;
        }
    }
    return str;
}

string dekripsi(int key, char str[])
{
    char temp;
    for (int i = 0; str[i] != '\0'; i++)
    {
        temp = str[i];
        if (temp >= 'a' && temp <= 'z') 
        {
            temp = temp - key;  
            if (temp > 'z')
            {
                temp = temp - 'z' + 'a' - 1;
            }
            str[i] = temp;
        }
        else if (temp >= 'A' && temp <= 'Z')
        {
            temp = temp - key;
            if (temp > 'Z')
            {
                temp = temp - 'Z' + 'A' - 1;
            }
            str[i] = temp;
        }
    }
    return str;
}

int main()
{
    int key;
    int menu;
    char str[99];

    do
    {
        cout << "-----... SHIFT CIPHER ...----\n";
        cout << "Menu:\n";
        cout << "1. Enkripsi\n";
        cout << "2. Dekripsi\n";
        cout << "3. Exit\n";
        cout << "Input Opsi: ";
        cin >> menu;
        cout << endl;

        switch (menu)
        {
        case 1:
            cout << "Silahkan Input Kata : ";
            cin.ignore(100, '\n');
            cin.getline(str, sizeof(str));
            cout << "Silahkan Input Key : ";
            cin >> key;
            cout << "Output Enkripsi : " << enkripsi(key, str) << endl;
            system("pause");
            system("cls");
            break;
        case 2:
            cout << "Silahkan Input Kata : ";
            cin.ignore(100, '\n');
            cin.getline(str, sizeof(str));
            cout << "Silahkan Input Key : ";
            cin >> key;
            cout << "Output Dekripsi : " << dekripsi(key, str) << endl;
            system("pause");
            system("cls");
            break;
        case 3:
            cout << "Terima kasih sudah menggunakan program ini!\n";
            cout << "....exit program. \n";
            break;
        default:
            cout << "Wrong Input!\n\n";
            break;
        }
    } while (menu != 3);
}

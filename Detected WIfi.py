from PyQt5 import QtWidgets, QtCore, QtGui
from scapy.all import ARP, Ether, srp
from time import sleep
import sys
from Forma4ipa2 import Ui_MainWindow
from threading import Thread
import locale
import time
import os


class Window(QtWidgets.QMainWindow, Ui_MainWindow):

    def __init__(self):
        super().__init__()
        self.setFixedSize(1119, 798)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.potor)
        self.pushButton_2.clicked.connect(self.connect)
        self.pushButton_4.clicked.connect(self.stop_scan)
        self.pushButton_3.clicked.connect(self.new_ip)
        self.action_2.triggered.connect(self.close)
        self.label_9.hide()
        self.label_12.hide()


        self.label_10.hide()
        self.label_11.hide()
        #лампочки
        self.label_8.hide()
        self.label_16.hide()

        self.label_3.hide()
        self.label_4.hide()
        self.label_5.hide()
        self.groupBox.hide()
        self.pushButton_3.setEnabled(False)
        self.pushButton_4.setEnabled(False)


        locale.setlocale(locale.LC_ALL,'ru_RU.UTF-8')
        self.g = "Час: %H: %M: %S"


    def potor(self):
        self.th3 = Thread(target=self.scan_wifi)
        self.th3.setDaemon(True)
        self.th3.start()

    def connect(self):

        self.label_7.setText("")

        self.host = self.lineEdit.text()

        if not self.host:
            print("Введіть значення")
            self.label_7.setText("Введіть IP сканувальної мережі (ПРИКЛАД: 192.168.1.0/24) ")
            sleep(0.5)
            return None
        self.pushButton_2.hide()
        self.groupBox.show()
        self.lineEdit.hide()
        self.label_7.hide()

    def stop_scan(self):
        self.K = False
        self.label_3.hide()
        self.pushButton.setEnabled(True)
        self.pushButton_4.setEnabled(False)
        self.pushButton_3.setEnabled(True)

    def new_ip(self):
        self.label_7.setText("Введіть IP сканувальної мережі (ПРИКЛАД: 192.168.1.0/24) ")
        self.K = False
        self.groupBox.hide()
        self.label_3.hide()
        self.lineEdit.show()
        self.label_7.show()
        self.pushButton_2.show()


    def scan_wifi(self):
        self.pushButton_3.setEnabled(False)
        self.pushButton_4.setEnabled(True)
        self.label_3.show()
        self.pushButton.setEnabled(False)
        self.K = True
        while (self.K == True):
            target_ip = self.host
            # IP Address for the destination
            # create ARP packet
            arp = ARP(pdst=target_ip)
            # create the Ether broadcast packetч
            # ff:ff:ff:ff:ff:ff MAC address indicates broadcasting
            ether = Ether(dst="ff:ff:ff:ff:ff:ff")
            # stack them
            packet = ether / arp

            result = srp(packet, timeout=3, verbose=0)[0]

            # a list of clients, we will fill this in the upcoming loop
            clients = []


            for sent, received in result:
                # for each response, append ip and mac address to `clients` list
                clients.append({'ip': received.psrc, 'mac': received.hwsrc})

            # print clients

            print("Available devices in the network:")
            print("IP" + " " * 18 + "MAC")

            for client in clients:
                print("{:16}    {}".format(client['ip'], client['mac']))
                mamba = format(client['ip'])
                samba = format(client['mac'])

                if mamba == '192.168.225.183':

                    self.label_9.show()
                    self.label_8.show()
                    self.label_12.show()
                    self.label_19.setText(mamba)
                    self.textEdit.append("Підключення користувача IP: " + mamba +'\n'+ time.strftime(self.g))
                    sleep(2)
                    self.label_9.hide()
                    self.label_12.hide()
                    self.label_8.hide()

                elif mamba == '192.168.119.247':
                    self.label_10.show()
                    self.label_20.setText(mamba)
                    sleep(2)
                    self.label_10.hide()


                elif mamba != '192.168.225.247' and '192.168.119.183':
                    self.label_4.show()
                    self.label_11.show()
                    self.textEdit.append(time.strftime(self.g)+'\n' + "Невідоме підключення до мережі IP: " + mamba + '\n' +"MAC: " + samba + '\n')
                    #self.label_21.setText("IP" + mamba)
                    sleep(2)
                    self.label_4.hide()
                    self.label_11.hide()

                    f = open('target.txt', 'a')
                    f.write('\n' + time.strftime(self.g) + '\n' + "Невідоме підключення до мережі IP: " + mamba + '\n' + "MAC: " + samba + '\n')
                    f.close()
                    #self.K = False
                    #self.pushButton.setEnabled(True)

                # elif len(clients) == 2:
                #     try:
                #         self.label_11.show()
                #         print(clients[2])
                #         self.label_21.setText("IP" + str(clients[2]))
                #     except Exception as e:
                #         print(e)
                elif len(clients) == 3:
                    print("3 клієнт в мережі")


                sleep(0.5)


if __name__ == "__main__":

    app = QtWidgets.QApplication(sys.argv)
    os.getcwd()

    if not os.path.exists('target.txt'):
        filetext = open("target.txt","w+")
        filetext.close()
    wind = Window()
    wind.show()
    sys.exit(app.exec_())

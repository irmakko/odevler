using System;
using System.Net;
using System.Net.Sockets;
using System.Text;

namespace server08
{
    class UDPServer
    {
        static void Main(string[] args)
        {

            recvmsg();


        }

        static void recvmsg()
        {
            UdpClient udpServer = new UdpClient(12345);//dinlemeye basladı.
            Console.WriteLine("Dinliyor...");
            IPEndPoint clientEndPoint = new IPEndPoint(IPAddress.Any, 0);
            while (true)
            {
                byte[] receivedData = udpServer.Receive(ref clientEndPoint);
                string receivedText = Encoding.UTF8.GetString(receivedData);
                string responseText = receivedText + "(" + DateTime.Now.ToString("HH:mm") + ")";
                byte[] responseData = Encoding.UTF8.GetBytes(responseText);
                udpServer.Send(responseData, responseData.Length, clientEndPoint);
                Console.WriteLine("Alındı: " + responseText);
            }
        }
    }
}



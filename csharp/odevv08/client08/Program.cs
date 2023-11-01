using System;
using System.Net;
using System.Net.Sockets;
using System.Text;

namespace client08
{
    class UDPClient
    {
        static void Main(string[] args)
        {
            
            sendmsg("Hello world");
        }

       

        public static void sendmsg(string message)
        {
             UdpClient udpClient = new UdpClient();
            IPEndPoint serverEndPoint = new IPEndPoint(IPAddress.Loopback,12345);
            
            byte[] sendData = Encoding.UTF8.GetBytes(message);
            udpClient.Send(sendData, sendData.Length, serverEndPoint);
        }
       
    }
}

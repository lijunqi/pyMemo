from etcd.client import Client
import etcd3

if __name__ == "__main__":
##    cli = Client(host="cvbstexdata01-preprod.cle.ra.rockwell.com", port=2379)
#    cli = Client(host="cvbstexdata01.cle.ra.rockwell.com", port=2379)
#    root = cli.read("/", recursive=True)
#    for result in root.children:
#        print(result.key + ": " + str(result.value) + "\n")
#        if result.dir:
#            print('--------------------- VVV')
#            for child in result.children:
#                print(child.key + ": " + str(child.value) + "\n")
#            print('--------------------- ^^^')

##    cli3 = etcd3.client(host="10.199.47.161", port=2379)
#    cli3 = etcd3.client(host="cvbstexdata01-preprod.cle.ra.rockwell.com", port=2379)
    cli3 = etcd3.client(host="cvbstexdata01.cle.ra.rockwell.com", port=2379)
#    res = cli3.get("stexqtest/stexenvironments/Automated-L3z/RA_ENV_DUT")
    for (_, m) in cli3.get_all():
        print(str(m.key) + ": " + str(cli3.get(m.key)) + "\n")

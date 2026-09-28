net_config={
    "0001":{
        "ip": "192.168.0.2",
        "device":"Switch",
        "policy":"Deny All",
        "status": False
    },
     "0002":{
            "ip": "192.168.0.1",
            "device":"Firewall",
            "policy":"Avoid .2.3.4",
            "status": True
        },
      "0005":{
                 "ip": "192.168.0.3",
                 "device":"Router",
                 "policy":"Allow all",
                 "status":  False
             },
        "0006":{
                  "ip": "192.168.0.4",
                  "device":"Switch",
                  "policy":"Avoid .6.7.8",
                  "status": False
              },
          "0007":{
                    "ip": "192.168.0.",
                    "device":"Firewall",
                    "policy":"Avoid .9",
                    "lista":[1,5,6,2,3,3],
                    "status": True
                    
                }
      
    
}

#
#contenido=net_config.get("0007")
#listaA= contenido.get('lista')
#num=listaA[2]
#print(num)

#print(net_config.get("0007").get("lista")[0])

#print(net_config.get("0001"))
#print(net_config.get("0000"))

#a=[1,2,3,[7.8,1]]
#print(a[3][1])

#net_config['0009']={"ip":1}
#print(net_config)



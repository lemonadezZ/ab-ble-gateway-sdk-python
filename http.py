import tornado.ioloop
import tornado.web
from enum   import Enum
import  abBleGatewaySdkPython as gateway

class advDataTypes(Enum):
	pass;

class advDataTypes(Enum):
	flags                               = 0x01
        service_16bit_uuid_more_available   = 0x02
        service_16bit_uuid_complete         = 0x03
        service_32bit_uuid_more_available   = 0x04
        service_32bit_uuid_complete         = 0x05
        service_128bit_uuid_more_available  = 0x06
        service_128bit_uuid_complete        = 0x07
        short_local_name                    = 0x08
        complete_local_name                 = 0x09
        tx_power_level                      = 0x10
        class_of_device                     = 0x11
        simple_pairing_hash_c               = 0x12
        simple_pairing_randimizer_r         = 0x13
        security_manager_tk_value           = 0x14
        security_manager_oob_flags          = 0x15
        slave_connection_interval_range     = 0x16
        solicited_sevice_uuids_16bit        = 0x17
        solicited_sevice_uuids_128bit       = 0x18
        service_data                        = 0x19
        public_target_address               = 0x20
        random_target_address               = 0x21
        appearance                          = 0x22
        advertising_interval                = 0x23
        le_bluetooth_device_address         = 0x24
        le_role                             = 0x25
        simple_pairng_hash_c256             = 0x26
        simple_pairng_randomizer_r256       = 0x27
        service_data_32bit_uuid             = 0x28
        service_data_128bit_uuid            = 0x29
        uri                                 = 0x30
	information_3d_data                 = 0x31
        manufacturer_specific_data          = 0x32

#types=advDataTypes();
#print types[1];

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("success")
    def post(self):
	package=self.request.files['chunk'][0]['body'];
	#print(payloads);
	print(gateway.decode(package));

if __name__ == "__main__":
    application = tornado.web.Application([
        (r"/", MainHandler),
    ])
    application.listen(8080)
    tornado.ioloop.IOLoop.current().start()

# -*- coding: utf-8 -*-

from typing import Dict


uuid16_dict = {
    0x0001: "SDP",
    0x0003: "RFCOMM",
    0x0005: "TCS-BIN",
    0x0007: "ATT",
    0x0008: "OBEX",
    0x000F: "BNEP",
    0x0010: "UPNP",
    0x0011: "HIDP",
    0x0012: "Hardcopy Control Channel",
    0x0014: "Hardcopy Data Channel",
    0x0016: "Hardcopy Notification",
    0x0017: "AVCTP",
    0x0019: "AVDTP",
    0x001B: "CMTP",
    0x001E: "MCAP Control Channel",
    0x001F: "MCAP Data Channel",
    0x0100: "L2CAP",
    # 0x0101 to 0x0fff undefined */
    0x1000: "Service Discovery Server Service Class",
    0x1001: "Browse Group Descriptor Service Class",
    0x1002: "Public Browse Root",
    # 0x1003 to 0x1100 undefined */
    0x1101: "Serial Port",
    0x1102: "LAN Access Using PPP",
    0x1103: "Dialup Networking",
    0x1104: "IrMC Sync",
    0x1105: "OBEX Object Push",
    0x1106: "OBEX File Transfer",
    0x1107: "IrMC Sync Command",
    0x1108: "Headset",
    0x1109: "Cordless Telephony",
    0x110A: "Audio Source",
    0x110B: "Audio Sink",
    0x110C: "A/V Remote Control Target",
    0x110D: "Advanced Audio Distribution",
    0x110E: "A/V Remote Control",
    0x110F: "A/V Remote Control Controller",
    0x1110: "Intercom",
    0x1111: "Fax",
    0x1112: "Headset AG",
    0x1113: "WAP",
    0x1114: "WAP Client",
    0x1115: "PANU",
    0x1116: "NAP",
    0x1117: "GN",
    0x1118: "Direct Printing",
    0x1119: "Reference Printing",
    0x111A: "Basic Imaging Profile",
    0x111B: "Imaging Responder",
    0x111C: "Imaging Automatic Archive",
    0x111D: "Imaging Referenced Objects",
    0x111E: "Handsfree",
    0x111F: "Handsfree Audio Gateway",
    0x1120: "Direct Printing Refrence Objects Service",
    0x1121: "Reflected UI",
    0x1122: "Basic Printing",
    0x1123: "Printing Status",
    0x1124: "Human Interface Device Service",
    0x1125: "Hardcopy Cable Replacement",
    0x1126: "HCR Print",
    0x1127: "HCR Scan",
    0x1128: "Common ISDN Access",
    # 0x1129 and 0x112a undefined */
    0x112D: "SIM Access",
    0x112E: "Phonebook Access Client",
    0x112F: "Phonebook Access Server",
    0x1130: "Phonebook Access",
    0x1131: "Headset HS",
    0x1132: "Message Access Server",
    0x1133: "Message Notification Server",
    0x1134: "Message Access Profile",
    0x1135: "GNSS",
    0x1136: "GNSS Server",
    0x1137: "3D Display",
    0x1138: "3D Glasses",
    0x1139: "3D Synchronization",
    0x113A: "MPS Profile",
    0x113B: "MPS Service",
    # 0x113c to 0x11ff undefined */
    0x1200: "PnP Information",
    0x1201: "Generic Networking",
    0x1202: "Generic File Transfer",
    0x1203: "Generic Audio",
    0x1204: "Generic Telephony",
    0x1205: "UPNP Service",
    0x1206: "UPNP IP Service",
    0x1300: "UPNP IP PAN",
    0x1301: "UPNP IP LAP",
    0x1302: "UPNP IP L2CAP",
    0x1303: "Video Source",
    0x1304: "Video Sink",
    0x1305: "Video Distribution",
    # 0x1306 to 0x13ff undefined */
    0x1400: "HDP",
    0x1401: "HDP Source",
    0x1402: "HDP Sink",
    # 0x1403 to 0x17ff undefined */
    0x1800: "Generic Access Profile",
    0x1801: "Generic Attribute Profile",
    0x1802: "Immediate Alert",
    0x1803: "Link Loss",
    0x1804: "Tx Power",
    0x1805: "Current Time Service",
    0x1806: "Reference Time Update Service",
    0x1807: "Next DST Change Service",
    0x1808: "Glucose",
    0x1809: "Health Thermometer",
    0x180A: "Device Information",
    # 0x180b and 0x180c undefined */
    0x180D: "Heart Rate",
    0x180E: "Phone Alert Status Service",
    0x180F: "Battery Service",
    0x1810: "Blood Pressure",
    0x1811: "Alert Notification Service",
    0x1812: "Human Interface Device",
    0x1813: "Scan Parameters",
    0x1814: "Running Speed and Cadence",
    0x1815: "Automation IO",
    0x1816: "Cycling Speed and Cadence",
    # 0x1817 undefined */
    0x1818: "Cycling Power",
    0x1819: "Location and Navigation",
    0x181A: "Environmental Sensing",
    0x181B: "Body Composition",
    0x181C: "User Data",
    0x181D: "Weight Scale",
    0x181E: "Bond Management",
    0x181F: "Continuous Glucose Monitoring",
    0x1820: "Internet Protocol Support",
    0x1821: "Indoor Positioning",
    0x1822: "Pulse Oximeter",
    0x1823: "HTTP Proxy",
    0x1824: "Transport Discovery",
    0x1825: "Object Transfer",
    0x1826: "Fitness Machine",
    0x1827: "Mesh Provisioning",
    0x1828: "Mesh Proxy",
    # 0x1829 to 0x27ff undefined */
    0x2800: "Primary Service",
    0x2801: "Secondary Service",
    0x2802: "Include",
    0x2803: "Characteristic",
    # 0x2804 to 0x28ff undefined */
    # Descriptors (SIG)
    0x2900: "Characteristic Extended Properties",
    0x2901: "Characteristic User Description",
    0x2902: "Client Characteristic Configuration",
    0x2903: "Server Characteristic Configuration",
    0x2904: "Characteristic Presentation Format",
    0x2905: "Characteristic Aggregate Format",
    0x2906: "Valid Range",
    0x2907: "External Report Reference",
    0x2908: "Report Reference",
    0x2909: "Number of Digitals",
    0x290A: "Value Trigger Setting",
    0x290B: "Environmental Sensing Configuration",
    0x290C: "Environmental Sensing Measurement",
    0x290D: "Environmental Sensing Trigger Setting",
    0x290E: "Time Trigger Setting",
    # 0x290f to 0x29ff undefined */
    0x2A00: "Device Name",
    0x2A01: "Appearance",
    0x2A02: "Peripheral Privacy Flag",
    0x2A03: "Reconnection Address",
    0x2A04: "Peripheral Preferred Connection Parameters",
    0x2A05: "Service Changed",
    0x2A06: "Alert Level",
    0x2A07: "Tx Power Level",
    0x2A08: "Date Time",
    0x2A09: "Day of Week",
    0x2A0A: "Day Date Time",
    0x2A0B: "Exact Time 100",
    0x2A0C: "Exact Time 256",
    0x2A0D: "DST Offset",
    0x2A0E: "Time Zone",
    0x2A0F: "Local Time Information",
    # 0x2a10 undefined */
    0x2A11: "Time with DST",
    0x2A12: "Time Accuracy",
    0x2A13: "Time Source",
    0x2A14: "Reference Time Information",
    # 0x2a15 undefined */
    0x2A16: "Time Update Control Point",
    0x2A17: "Time Update State",
    0x2A18: "Glucose Measurement",
    0x2A19: "Battery Level",
    0x2A1A: "Battery Power State",
    0x2A1B: "Battery Level State",
    0x2A1C: "Temperature Measurement",
    0x2A1D: "Temperature Type",
    0x2A1E: "Intermediate Temperature",
    0x2A1F: "Temperature Celsius",
    0x2A20: "Temperature Fahrenheit",
    0x2A21: "Measurement Interval",
    0x2A22: "Boot Keyboard Input Report",
    0x2A23: "System ID",
    0x2A24: "Model Number String",
    0x2A25: "Serial Number String",
    0x2A26: "Firmware Revision String",
    0x2A27: "Hardware Revision String",
    0x2A28: "Software Revision String",
    0x2A29: "Manufacturer Name String",
    0x2A2A: "IEEE 11073-20601 Regulatory Cert. Data List",
    0x2A2B: "Current Time",
    0x2A2C: "Magnetic Declination",
    # 0x2a2d to 0x2a30 undefined */
    0x2A31: "Scan Refresh",
    0x2A32: "Boot Keyboard Output Report",
    0x2A33: "Boot Mouse Input Report",
    0x2A34: "Glucose Measurement Context",
    0x2A35: "Blood Pressure Measurement",
    0x2A36: "Intermediate Cuff Pressure",
    0x2A37: "Heart Rate Measurement",
    0x2A38: "Body Sensor Location",
    0x2A39: "Heart Rate Control Point",
    # 0x2a3a to 0x2a3e undefined */
    0x2A3F: "Alert Status",
    0x2A40: "Ringer Control Point",
    0x2A41: "Ringer Setting",
    0x2A42: "Alert Category ID Bit Mask",
    0x2A43: "Alert Category ID",
    0x2A44: "Alert Notification Control Point",
    0x2A45: "Unread Alert Status",
    0x2A46: "New Alert",
    0x2A47: "Supported New Alert Category",
    0x2A48: "Supported Unread Alert Category",
    0x2A49: "Blood Pressure Feature",
    0x2A4A: "HID Information",
    0x2A4B: "Report Map",
    0x2A4C: "HID Control Point",
    0x2A4D: "Report",
    0x2A4E: "Protocol Mode",
    0x2A4F: "Scan Interval Window",
    0x2A50: "PnP ID",
    0x2A51: "Glucose Feature",
    0x2A52: "Record Access Control Point",
    0x2A53: "RSC Measurement",
    0x2A54: "RSC Feature",
    0x2A55: "SC Control Point",
    0x2A56: "Digital",
    # 0x2a57 undefined */
    0x2A58: "Analog",
    # 0x2a59 undefined */
    0x2A5A: "Aggregate",
    0x2A5B: "CSC Measurement",
    0x2A5C: "CSC Feature",
    0x2A5D: "Sensor Location",
    # 0x2a5e to 0x2a62 undefined */
    0x2A63: "Cycling Power Measurement",
    0x2A64: "Cycling Power Vector",
    0x2A65: "Cycling Power Feature",
    0x2A66: "Cycling Power Control Point",
    0x2A67: "Location and Speed",
    0x2A68: "Navigation",
    0x2A69: "Position Quality",
    0x2A6A: "LN Feature",
    0x2A6B: "LN Control Point",
    0x2A6C: "Elevation",
    0x2A6D: "Pressure",
    0x2A6E: "Temperature",
    0x2A6F: "Humidity",
    0x2A70: "True Wind Speed",
    0x2A71: "True Wind Direction",
    0x2A72: "Apparent Wind Speed",
    0x2A73: "Apparent Wind Direction",
    0x2A74: "Gust Factor",
    0x2A75: "Pollen Concentration",
    0x2A76: "UV Index",
    0x2A77: "Irradiance",
    0x2A78: "Rainfall",
    0x2A79: "Wind Chill",
    0x2A7A: "Heat Index",
    0x2A7B: "Dew Point",
    0x2A7C: "Trend",
    0x2A7D: "Descriptor Value Changed",
    0x2A7E: "Aerobic Heart Rate Lower Limit",
    0x2A7F: "Aerobic Threshold",
    0x2A80: "Age",
    0x2A81: "Anaerobic Heart Rate Lower Limit",
    0x2A82: "Anaerobic Heart Rate Upper Limit",
    0x2A83: "Anaerobic Threshold",
    0x2A84: "Aerobic Heart Rate Upper Limit",
    0x2A85: "Date of Birth",
    0x2A86: "Date of Threshold Assessment",
    0x2A87: "Email Address",
    0x2A88: "Fat Burn Heart Rate Lower Limit",
    0x2A89: "Fat Burn Heart Rate Upper Limit",
    0x2A8A: "First Name",
    0x2A8B: "Five Zone Heart Rate Limits",
    0x2A8C: "Gender",
    0x2A8D: "Heart Rate Max",
    0x2A8E: "Height",
    0x2A8F: "Hip Circumference",
    0x2A90: "Last Name",
    0x2A91: "Maximum Recommended Heart Rate",
    0x2A92: "Resting Heart Rate",
    0x2A93: "Sport Type for Aerobic/Anaerobic Thresholds",
    0x2A94: "Three Zone Heart Rate Limits",
    0x2A95: "Two Zone Heart Rate Limit",
    0x2A96: "VO2 Max",
    0x2A97: "Waist Circumference",
    0x2A98: "Weight",
    0x2A99: "Database Change Increment",
    0x2A9A: "User Index",
    0x2A9B: "Body Composition Feature",
    0x2A9C: "Body Composition Measurement",
    0x2A9D: "Weight Measurement",
    0x2A9E: "Weight Scale Feature",
    0x2A9F: "User Control Point",
    0x2AA0: "Magnetic Flux Density - 2D",
    0x2AA1: "Magnetic Flux Density - 3D",
    0x2AA2: "Language",
    0x2AA3: "Barometric Pressure Trend",
    0x2AA4: "Bond Management Control Point",
    0x2AA5: "Bond Management Feature",
    0x2AA6: "Central Address Resolution",
    0x2AA7: "CGM Measurement",
    0x2AA8: "CGM Feature",
    0x2AA9: "CGM Status",
    0x2AAA: "CGM Session Start Time",
    0x2AAB: "CGM Session Run Time",
    0x2AAC: "CGM Specific Ops Control Point",
    0x2AAD: "Indoor Positioning Configuration",
    0x2AAE: "Latitude",
    0x2AAF: "Longitude",
    0x2AB0: "Local North Coordinate",
    0x2AB1: "Local East Coordinate",
    0x2AB2: "Floor Number",
    0x2AB3: "Altitude",
    0x2AB4: "Uncertainty",
    0x2AB5: "Location Name",
    0x2AB6: "URI",
    0x2AB7: "HTTP Headers",
    0x2AB8: "HTTP Status Code",
    0x2AB9: "HTTP Entity Body",
    0x2ABA: "HTTP Control Point",
    0x2ABB: "HTTPS Security",
    0x2ABC: "TDS Control Point",
    0x2ABD: "OTS Feature",
    0x2ABE: "Object Name",
    0x2ABF: "Object Type",
    0x2AC0: "Object Size",
    0x2AC1: "Object First-Created",
    0x2AC2: "Object Last-Modified",
    0x2AC3: "Object ID",
    0x2AC4: "Object Properties",
    0x2AC5: "Object Action Control Point",
    0x2AC6: "Object List Control Point",
    0x2AC7: "Object List Filter",
    0x2AC8: "Object Changed",
    0x2AC9: "Resolvable Private Address Only",
    # 0x2aca and 0x2acb undefined */
    0x2ACC: "Fitness Machine Feature",
    0x2ACD: "Treadmill Data",
    0x2ACE: "Cross Trainer Data",
    0x2ACF: "Step Climber Data",
    0x2AD0: "Stair Climber Data",
    0x2AD1: "Rower Data",
    0x2AD2: "Indoor Bike Data",
    0x2AD3: "Training Status",
    0x2AD4: "Supported Speed Range",
    0x2AD5: "Supported Inclination Range",
    0x2AD6: "Supported Resistance Level Range",
    0x2AD7: "Supported Heart Rate Range",
    0x2AD8: "Supported Power Range",
    0x2AD9: "Fitness Machine Control Point",
    0x2ADA: "Fitness Machine Status",
    0x2ADB: "Mesh Provisioning Data In",
    0x2ADC: "Mesh Provisioning Data Out",
    0x2ADD: "Mesh Proxy Data In",
    0x2ADE: "Mesh Proxy Data Out",
    0x2A59: "Analog Output",
    0x2B29: "Client Supported Features",
    0x2B2A: "Database Hash",
    0x2AED: "Date UTC",
    0x2A57: "Digital Output",
    0x2B22: "IDD Annunciation Status",
    0x2B25: "IDD Command Control Point",
    0x2B26: "IDD Command Data",
    0x2B23: "IDD Features",
    0x2B28: "IDD History Data",
    0x2B27: "IDD Record Access Control Point",
    0x2B21: "IDD Status",
    0x2B20: "IDD Status Changed",
    0x2B24: "IDD Status Reader Control Point",
    0x2A3E: "Network Availability",
    0x2A5F: "PLX Continuous Measurement Characteristic",
    0x2A60: "PLX Features",
    0x2A5E: "PLX Spot-Check Measurement",
    0x2A2F: "Position 2D",
    0x2A30: "Position 3D",
    0x2A62: "Pulse Oximetry Control Point",
    0x2B1D: "RC Feature",
    0x2B1E: "RC Settings",
    0x2B1F: "Reconnection Configuration Control Point",
    0x2A3A: "Removable",
    0x2A3C: "Scientific Temperature Celsius",
    0x2A10: "Secondary Time Zone",
    0x2A3B: "Service Required",
    0x2A3D: "String",
    0x2A15: "Time Broadcast",
    # vendor defined */
    0xFEFF: "GN Netcom",
    0xFEFE: "GN ReSound A/S",
    0xFEFD: "Gimbal: Inc.",
    0xFEFC: "Gimbal: Inc.",
    0xFEFB: "Stollmann E+V GmbH",
    0xFEFA: "PayPal: Inc.",
    0xFEF9: "PayPal: Inc.",
    0xFEF8: "Aplix Corporation",
    0xFEF7: "Aplix Corporation",
    0xFEF6: "Wicentric: Inc.",
    0xFEF5: "Dialog Semiconductor GmbH",
    0xFEF4: "Google",
    0xFEF3: "Google",
    0xFEF2: "CSR",
    0xFEF1: "CSR",
    0xFEF0: "Intel",
    0xFEEF: "Polar Electro Oy",
    0xFEEE: "Polar Electro Oy",
    0xFEED: "Tile: Inc.",
    0xFEEC: "Tile: Inc.",
    0xFEEB: "Swirl Networks: Inc.",
    0xFEEA: "Swirl Networks: Inc.",
    0xFEE9: "Quintic Corp.",
    0xFEE8: "Quintic Corp.",
    0xFEE7: "Tencent Holdings Limited",
    0xFEE6: "Seed Labs: Inc.",
    0xFEE5: "Nordic Semiconductor ASA",
    0xFEE4: "Nordic Semiconductor ASA",
    0xFEE3: "Anki: Inc.",
    0xFEE2: "Anki: Inc.",
    0xFEE1: "Anhui Huami Information Technology Co.",
    0xFEE0: "Anhui Huami Information Technology Co.",
    0xFEDF: "Design SHIFT",
    0xFEDE: "Coin: Inc.",
    0xFEDD: "Jawbone",
    0xFEDC: "Jawbone",
    0xFEDB: "Perka: Inc.",
    0xFEDA: "ISSC Technologies Corporation",
    0xFED9: "Pebble Technology Corporation",
    0xFED8: "Google",
    0xFED7: "Broadcom Corporation",
    0xFED6: "Broadcom Corporation",
    0xFED5: "Plantronics Inc.",
    0xFED4: "Apple: Inc.",
    0xFED3: "Apple: Inc.",
    0xFED2: "Apple: Inc.",
    0xFED1: "Apple: Inc.",
    0xFED0: "Apple: Inc.",
    0xFECF: "Apple: Inc.",
    0xFECE: "Apple: Inc.",
    0xFECD: "Apple: Inc.",
    0xFECC: "Apple: Inc.",
    0xFECB: "Apple: Inc.",
    0xFECA: "Apple: Inc.",
    0xFEC9: "Apple: Inc.",
    0xFEC8: "Apple: Inc.",
    0xFEC7: "Apple: Inc.",
    0xFEC6: "Kocomojo: LLC",
    0xFEC5: "Realtek Semiconductor Corp.",
    0xFEC4: "PLUS Location Systems",
    0xFEC3: "360fly: Inc.",
    0xFEC2: "Blue Spark Technologies: Inc.",
    0xFEC1: "KDDI Corporation",
    0xFEC0: "KDDI Corporation",
    0xFEBF: "Nod: Inc.",
    0xFEBE: "Bose Corporation",
    0xFEBD: "Clover Network: Inc.",
    0xFEBC: "Dexcom: Inc.",
    0xFEBB: "adafruit industries",
    0xFEBA: "Tencent Holdings Limited",
    0xFEB9: "LG Electronics",
    0xFEB8: "Facebook: Inc.",
    0xFEB7: "Facebook: Inc.",
    0xFEB6: "Vencer Co: Ltd",
    0xFEB5: "WiSilica Inc.",
    0xFEB4: "WiSilica Inc.",
    0xFEB3: "Taobao",
    0xFEB2: "Microsoft Corporation",
    0xFEB1: "Electronics Tomorrow Limited",
    0xFEB0: "Nest Labs Inc.",
    0xFEAF: "Nest Labs Inc.",
    0xFEAE: "Nokia Corporation",
    0xFEAD: "Nokia Corporation",
    0xFEAC: "Nokia Corporation",
    0xFEAB: "Nokia Corporation",
    0xFEAA: "Google",
    0xFEA9: "Savant Systems LLC",
    0xFEA8: "Savant Systems LLC",
    0xFEA7: "UTC Fire and Security",
    0xFEA6: "GoPro: Inc.",
    0xFEA5: "GoPro: Inc.",
    0xFEA4: "Paxton Access Ltd",
    0xFEA3: "ITT Industries",
    0xFEA2: "Intrepid Control Systems: Inc.",
    0xFEA1: "Intrepid Control Systems: Inc.",
    0xFEA0: "Google",
    0xFE9F: "Google",
    0xFE9E: "Dialog Semiconductor B.V.",
    0xFE9D: "Mobiquity Networks Inc",
    0xFE9C: "GSI Laboratories: Inc.",
    0xFE9B: "Samsara Networks: Inc",
    0xFE9A: "Estimote",
    0xFE99: "Currant: Inc.",
    0xFE98: "Currant: Inc.",
    0xFE97: "Tesla Motor Inc.",
    0xFE96: "Tesla Motor Inc.",
    0xFE95: "Xiaomi Inc.",
    0xFE94: "OttoQ Inc.",
    0xFE93: "OttoQ Inc.",
    0xFE92: "Jarden Safety & Security",
    0xFE91: "Shanghai Imilab Technology Co.,Ltd",
    0xFE90: "JUMA",
    0xFE8F: "CSR",
    0xFE8E: "ARM Ltd",
    0xFE8D: "Interaxon Inc.",
    0xFE8C: "TRON Forum",
    0xFE8B: "Apple: Inc.",
    0xFE8A: "Apple: Inc.",
    0xFE89: "B&O Play A/S",
    0xFE88: "SALTO SYSTEMS S.L.",
    0xFE87: "Qingdao Yeelink Information Technology Co.: Ltd. ( 青岛亿联客信息技术有限公司 )",
    0xFE86: "HUAWEI Technologies Co.: Ltd. ( 华为技术有限公司 )",
    0xFE85: "RF Digital Corp",
    0xFE84: "RF Digital Corp",
    0xFE83: "Blue Bite",
    0xFE82: "Medtronic Inc.",
    0xFE81: "Medtronic Inc.",
    0xFE80: "Doppler Lab",
    0xFE7F: "Doppler Lab",
    0xFE7E: "Awear Solutions Ltd",
    0xFE7D: "Aterica Health Inc.",
    0xFE7C: "Stollmann E+V GmbH",
    0xFE7B: "Orion Labs: Inc.",
    0xFE7A: "Bragi GmbH",
    0xFE79: "Zebra Technologies",
    0xFE78: "Hewlett-Packard Company",
    0xFE77: "Hewlett-Packard Company",
    0xFE76: "TangoMe",
    0xFE75: "TangoMe",
    0xFE74: "unwire",
    0xFE73: "St. Jude Medical: Inc.",
    0xFE72: "St. Jude Medical: Inc.",
    0xFE71: "Plume Design Inc",
    0xFE70: "Beijing Jingdong Century Trading Co.: Ltd.",
    0xFE6F: "LINE Corporation",
    0xFE6E: "The University of Tokyo",
    0xFE6D: "The University of Tokyo",
    0xFE6C: "TASER International: Inc.",
    0xFE6B: "TASER International: Inc.",
    0xFE6A: "Kontakt Micro-Location Sp. z o.o.",
    0xFE69: "Qualcomm Life Inc",
    0xFE68: "Qualcomm Life Inc",
    0xFE67: "Lab Sensor Solutions",
    0xFE66: "Intel Corporation",
    0xFE65: "CHIPOLO d.o.o.",
    0xFE64: "Siemens AG",
    0xFE63: "Connected Yard: Inc.",
    0xFE62: "Indagem Tech LLC",
    0xFE61: "Logitech International SA",
    0xFE60: "Lierda Science & Technology Group Co.: Ltd.",
    0xFE5F: "Eyefi: Inc.",
    0xFE5E: "Plastc Corporation",
    0xFE5D: "Grundfos A/S",
    0xFE5C: "million hunters GmbH",
    0xFE5B: "GT-tronics HK Ltd",
    0xFE5A: "Chronologics Corporation",
    0xFE59: "Nordic Semiconductor ASA",
    0xFE58: "Nordic Semiconductor ASA",
    0xFE57: "Dotted Labs",
    0xFE56: "Google Inc.",
    0xFE55: "Google Inc.",
    0xFE54: "Motiv: Inc.",
    0xFE53: "3M",
    0xFE52: "SetPoint Medical",
    0xFE51: "SRAM",
    0xFE50: "Google Inc.",
    0xFE4F: "Molekule: Inc.",
    0xFE4E: "NTT docomo",
    0xFE4D: "Casambi Technologies Oy",
    0xFE4C: "Volkswagen AG",
    0xFE4B: "Koninklijke Philips N.V.",
    0xFE4A: "OMRON HEALTHCARE Co.: Ltd.",
    0xFE49: "SenionLab AB",
    0xFE48: "General Motors",
    0xFE47: "General Motors",
    0xFE46: "B&O Play A/S",
    0xFE45: "Snapchat Inc",
    0xFE44: "SK Telecom",
    0xFE43: "Andreas Stihl AG & Co. KG",
    0xFE42: "Nets A/S",
    0xFE41: "Inugo Systems Limited",
    0xFE40: "Inugo Systems Limited",
    0xFE3F: "Friday Labs Limited",
    0xFE3E: "BD Medical",
    0xFE3D: "BD Medical",
    0xFE3C: "Alibaba",
    0xFE3B: "Dolby Laboratories",
    0xFE3A: "TTS Tooltechnic Systems AG & Co. KG",
    0xFE39: "TTS Tooltechnic Systems AG & Co. KG",
    0xFE38: "Spaceek LTD",
    0xFE37: "Spaceek LTD",
    0xFE36: "HUAWEI Technologies Co.: Ltd",
    0xFE35: "HUAWEI Technologies Co.: Ltd",
    0xFE34: "SmallLoop LLC",
    0xFE33: "CHIPOLO d.o.o.",
    0xFE32: "Pro-Mark: Inc.",
    0xFE31: "Volkswagen AG",
    0xFE30: "Volkswagen AG",
    0xFE2F: "CRESCO Wireless: Inc",
    0xFE2E: "ERi,Inc.",
    0xFE2D: "SMART INNOVATION Co.,Ltd",
    0xFE2C: "Google Inc.",
    0xFE2B: "ITT Industries",
    0xFE2A: "DaisyWorks: Inc.",
    0xFE29: "Gibson Innovations",
    0xFE28: "Ayla Network",
    0xFE27: "Google Inc.",
    0xFE26: "Google Inc.",
    0xFE25: "Apple: Inc.",
    0xFE24: "August Home Inc",
    0xFE23: "Zoll Medical Corporation",
    0xFE22: "Zoll Medical Corporation",
    0xFE21: "Bose Corporation",
    0xFE20: "Emerson",
    0xFE1F: "Garmin International: Inc.",
    0xFE1E: "Smart Innovations Co.: Ltd",
    0xFE1D: "Illuminati Instrument Corporation",
    0xFE1C: "NetMedia: Inc.",
    # SDO defined */
    0xFFFC: "AirFuel Alliance",
    0xFFFE: "Alliance for Wireless Power (A4WP)",
    0xFFFD: "Fast IDentity Online Alliance (FIDO)",
    # Mesh Characteristics
    0x2AE0: "Average Current",
    0x2AE1: "Average Voltage",
    0x2AE2: "Boolean",
    0x2AE3: "Chromatic Distance From Planckian",
    0x2B1C: "Chromaticity Coordinate",
    0x2AE4: "Chromaticity Coordinates",
    0x2AE5: "Chromaticity In CCT And Duv Values",
    0x2AE6: "Chromaticity Tolerance",
    0x2AE7: "CIE 13.3-1995 Color Rendering Index",
    0x2AE8: "Coefficient",
    0x2AE9: "Correlated Color Temperature",
    0x2AEA: "Count 16",
    0x2AEB: "Count 24",
    0x2AEC: "Country Code",
    0x2AED: "Date UTC",
    0x2AEE: "Electric Current",
    0x2AEF: "Electric Current Range",
    0x2AF0: "Electric Current Specification",
    0x2AF1: "Electric Current Statistics",
    0x2AF2: "Energy",
    0x2AF3: "Energy In A Period Of Day",
    0x2AF4: "Event Statistics",
    0x2AF5: "Fixed String 16",
    0x2AF6: "Fixed String 24",
    0x2AF7: "Fixed String 36",
    0x2AF8: "Fixed String 8",
    0x2AF9: "Generic Level",
    0x2AFA: "Global Trade Item Number",
    0x2AFB: "Illuminance",
    0x2AFC: "Luminous Efficacy",
    0x2AFD: "Luminous Energy",
    0x2AFE: "Luminous Exposure",
    0x2AFF: "Luminous Flux",
    0x2B00: "Luminous Flux Range",
    0x2B01: "Luminous Intensity",
    0x2B02: "Mass Flow",
    0x2ADB: "Mesh Provisioning Data In",
    0x2ADC: "Mesh Provisioning Data Out",
    0x2ADD: "Mesh Proxy Data In",
    0x2ADE: "Mesh Proxy Data Out",
    0x2B03: "Perceived Lightness",
    0x2B04: "Percentage 8",
    0x2B05: "Power",
    0x2B06: "Power Specification",
    0x2B07: "Relative Runtime In A Current Range",
    0x2B08: "Relative Runtime In A Generic Level Range",
    0x2B0B: "Relative Value In A Period of Day",
    0x2B0C: "Relative Value In A Temperature Range",
    0x2B09: "Relative Value In A Voltage Range",
    0x2B0A: "Relative Value In An Illuminance Range",
    0x2B0D: "Temperature 8",
    0x2B0E: "Temperature 8 In A Period Of Day",
    0x2B0F: "Temperature 8 Statistics",
    0x2B10: "Temperature Range",
    0x2B11: "Temperature Statistics",
    0x2B12: "Time Decihour 8",
    0x2B13: "Time Exponential 8",
    0x2B14: "Time Hour 24",
    0x2B15: "Time Millisecond 24",
    0x2B16: "Time Second 16",
    0x2B17: "Time Second 8",
    0x2B18: "Voltage",
    0x2B19: "Voltage Specification",
    0x2B1A: "Voltage Statistics",
    0x2B1B: "Volume Flow",
}

uuid128_dict = {
    "a3c87500-8ed3-4bdf-8a39-a01bebede295": "Eddystone Configuration Service",
    "a3c87501-8ed3-4bdf-8a39-a01bebede295": "Capabilities",
    "a3c87502-8ed3-4bdf-8a39-a01bebede295": "Active Slot",
    "a3c87503-8ed3-4bdf-8a39-a01bebede295": "Advertising Interval",
    "a3c87504-8ed3-4bdf-8a39-a01bebede295": "Radio Tx Power",
    "a3c87505-8ed3-4bdf-8a39-a01bebede295": "(Advanced) Advertised Tx Power",
    "a3c87506-8ed3-4bdf-8a39-a01bebede295": "Lock State",
    "a3c87507-8ed3-4bdf-8a39-a01bebede295": "Unlock",
    "a3c87508-8ed3-4bdf-8a39-a01bebede295": "Public ECDH Key",
    "a3c87509-8ed3-4bdf-8a39-a01bebede295": "EID Identity Key",
    "a3c8750a-8ed3-4bdf-8a39-a01bebede295": "ADV Slot Data",
    "a3c8750b-8ed3-4bdf-8a39-a01bebede295": "(Advanced) Factory reset",
    "a3c8750c-8ed3-4bdf-8a39-a01bebede295": "(Advanced) Remain Connectable",
    # BBC micro:bit Bluetooth Profiles */
    "e95d0753-251d-470a-a062-fa1922dfa9a8": "MicroBit Accelerometer Service",
    "e95dca4b-251d-470a-a062-fa1922dfa9a8": "MicroBit Accelerometer Data",
    "e95dfb24-251d-470a-a062-fa1922dfa9a8": "MicroBit Accelerometer Period",
    "e95df2d8-251d-470a-a062-fa1922dfa9a8": "MicroBit Magnetometer Service",
    "e95dfb11-251d-470a-a062-fa1922dfa9a8": "MicroBit Magnetometer Data",
    "e95d386c-251d-470a-a062-fa1922dfa9a8": "MicroBit Magnetometer Period",
    "e95d9715-251d-470a-a062-fa1922dfa9a8": "MicroBit Magnetometer Bearing",
    "e95d9882-251d-470a-a062-fa1922dfa9a8": "MicroBit Button Service",
    "e95dda90-251d-470a-a062-fa1922dfa9a8": "MicroBit Button A State",
    "e95dda91-251d-470a-a062-fa1922dfa9a8": "MicroBit Button B State",
    "e95d127b-251d-470a-a062-fa1922dfa9a8": "MicroBit IO PIN Service",
    "e95d8d00-251d-470a-a062-fa1922dfa9a8": "MicroBit PIN Data",
    "e95d5899-251d-470a-a062-fa1922dfa9a8": "MicroBit PIN AD Configuration",
    "e95dd822-251d-470a-a062-fa1922dfa9a8": "MicroBit PWM Control",
    "e95dd91d-251d-470a-a062-fa1922dfa9a8": "MicroBit LED Service",
    "e95d7b77-251d-470a-a062-fa1922dfa9a8": "MicroBit LED Matrix state",
    "e95d93ee-251d-470a-a062-fa1922dfa9a8": "MicroBit LED Text",
    "e95d0d2d-251d-470a-a062-fa1922dfa9a8": "MicroBit Scrolling Delay",
    "e95d93af-251d-470a-a062-fa1922dfa9a8": "MicroBit Event Service",
    "e95db84c-251d-470a-a062-fa1922dfa9a8": "MicroBit Requirements",
    "e95d9775-251d-470a-a062-fa1922dfa9a8": "MicroBit Event Data",
    "e95d23c4-251d-470a-a062-fa1922dfa9a8": "MicroBit Client Requirements",
    "e95d5404-251d-470a-a062-fa1922dfa9a8": "MicroBit Client Events",
    "e95d93b0-251d-470a-a062-fa1922dfa9a8": "MicroBit DFU Control Service" "",
    "e95d93b1-251d-470a-a062-fa1922dfa9a8": "MicroBit DFU Control",
    "e95d6100-251d-470a-a062-fa1922dfa9a8": "MicroBit Temperature Service",
    "e95d1b25-251d-470a-a062-fa1922dfa9a8": "MicroBit Temperature Period",
    # Nordic UART Port Emulation */
    "6e400001-b5a3-f393-e0a9-e50e24dcca9e": "Nordic UART Service",
    "6e400003-b5a3-f393-e0a9-e50e24dcca9e": "Nordic UART TX",
    "6e400002-b5a3-f393-e0a9-e50e24dcca9e": "Nordic UART RX",
    # LEGO
    "00001623-1212-efde-1623-785feabcd123": "LEGO Wireless Protocol v3 Hub Service",
    "00001624-1212-efde-1623-785feabcd123": "LEGO Wireless Protocol v3 Hub Characteristic",
    "00001625-1212-efde-1623-785feabcd123": "LEGO Wireless Protocol v3 Bootloader Service",
    "00001626-1212-efde-1623-785feabcd123": "LEGO Wireless Protocol v3 Bootloader Characteristic",
    "c5f50001-8280-46da-89f4-6d8051e4aeef": "Pybricks Service",
    "c5f50002-8280-46da-89f4-6d8051e4aeef": "Pybricks Characteristic",
    # from nRF connect
    "be15bee0-6186-407e-8381-0bd89c4d8df4": "Anki Drive Vehicle Service READ",
    "be15bee1-6186-407e-8381-0bd89c4d8df4": "Anki Drive Vehicle Service WRITE",
    "955a1524-0fe2-f5aa-a094-84b8d4f3e8ad": "Beacon UUID",
    "00001524-1212-efde-1523-785feabcd123": "Button",
    "8ec90003-f315-4f60-9fb8-838830daea50": "Buttonless DFU",
    "955a1525-0fe2-f5aa-a094-84b8d4f3e8ad": "Calibration",
    "a6c31338-6c07-453e-961a-d8a8a41bf368": "Candy Control Point",
    "955a1528-0fe2-f5aa-a094-84b8d4f3e8ad": "Connection Interval",
    "00001531-1212-efde-1523-785feabcd123": "DFU Control Point",
    "8ec90001-f315-4f60-9fb8-838830daea50": "DFU Control Point",
    "00001532-1212-efde-1523-785feabcd123": "DFU Packet",
    "8ec90002-f315-4f60-9fb8-838830daea50": "DFU Packet",
    "00001534-1212-efde-1523-785feabcd123": "DFU Version",
    "ee0c2084-8786-40ba-ab96-99b91ac981d8": "Data",
    "b35d7da9-eed4-4d59-8f89-f6573edea967": "Data Length",
    "b35d7da7-eed4-4d59-8f89-f6573edea967": "Data One",
    "22eac6e9-24d6-4bb5-be44-b36ace7c7bfb": "Data Source",
    "b35d7da8-eed4-4d59-8f89-f6573edea967": "Data Two",
    "c6b2f38c-23ab-46d8-a6ab-a3a870bbd5d7": "Entity Attribute",
    "2f7cabce-808d-411f-9a0c-bb92ba96c102": "Entity Update",
    "ee0c2085-8786-40ba-ab96-99b91ac981d8": "Flags",
    "88400002-e95a-844e-c53f-fbec32ed5e54": "Fly Button Characteristic",
    "00001525-1212-efde-1523-785feabcd123": "LED",
    "955a1529-0fe2-f5aa-a094-84b8d4f3e8ad": "LED Config",
    "ee0c2082-8786-40ba-ab96-99b91ac981d8": "Lock",
    "ee0c2081-8786-40ba-ab96-99b91ac981d8": "Lock State",
    "955a1526-0fe2-f5aa-a094-84b8d4f3e8ad": "Major & Minor",
    "955a1527-0fe2-f5aa-a094-84b8d4f3e8ad": "Manufacturer ID",
    "9fbf120d-6301-42d9-8c58-25e699a21dbd": "Notification Source",
    "ee0c2088-8786-40ba-ab96-99b91ac981d8": "Period",
    "ee0c2086-8786-40ba-ab96-99b91ac981d8": "Power Levels",
    "ee0c2087-8786-40ba-ab96-99b91ac981d8": "Power Mode",
    "9b3c81d8-57b1-4a8a-b8df-0e56f7ca51c2": "Remote Command",
    "ee0c2089-8786-40ba-ab96-99b91ac981d8": "Reset",
    "da2e7828-fbce-4e01-ae9e-261174997c48": "SMP Characteristic",
    "8ec90004-f315-4f60-9fb8-838830daea50": "Secure Buttonless DFU",
    "ef680102-9b35-4933-9b10-52ffa9740042": "Thingy Advertising Parameters Characteristic",
    "ef680204-9b35-4933-9b10-52ffa9740042": "Thingy Air Quality Characteristic",
    "ef680302-9b35-4933-9b10-52ffa9740042": "Thingy Button Characteristic",
    "ef680106-9b35-4933-9b10-52ffa9740042": "Thingy Cloud Token Characteristic",
    "ef680104-9b35-4933-9b10-52ffa9740042": "Thingy Connection Parameters Characteristic",
    "ef680105-9b35-4933-9b10-52ffa9740042": "Thingy Eddystone URL Characteristic",
    "ef680206-9b35-4933-9b10-52ffa9740042": "Thingy Environment Configuration Characteristic",
    "ef680407-9b35-4933-9b10-52ffa9740042": "Thingy Euler Characteristic",
    "ef680303-9b35-4933-9b10-52ffa9740042": "Thingy External Pin Characteristic",
    "ef680107-9b35-4933-9b10-52ffa9740042": "Thingy FW Version Characteristic",
    "ef68040a-9b35-4933-9b10-52ffa9740042": "Thingy Gravity Vector Characteristic",
    "ef680409-9b35-4933-9b10-52ffa9740042": "Thingy Heading Characteristic",
    "ef680203-9b35-4933-9b10-52ffa9740042": "Thingy Humidity Characteristic",
    "ef680301-9b35-4933-9b10-52ffa9740042": "Thingy LED Characteristic",
    "ef680205-9b35-4933-9b10-52ffa9740042": "Thingy Light Intensity Characteristic",
    "ef680108-9b35-4933-9b10-52ffa9740042": "Thingy MTU Request Characteristic",
    "ef680504-9b35-4933-9b10-52ffa9740042": "Thingy Microphone Characteristic",
    "ef680401-9b35-4933-9b10-52ffa9740042": "Thingy Motion Configuration Characteristic",
    "ef680101-9b35-4933-9b10-52ffa9740042": "Thingy Name Characteristic",
    "ef680403-9b35-4933-9b10-52ffa9740042": "Thingy Orientation Characteristic",
    "ef680405-9b35-4933-9b10-52ffa9740042": "Thingy Pedometer Characteristic",
    "ef680202-9b35-4933-9b10-52ffa9740042": "Thingy Pressure Characteristic",
    "ef680404-9b35-4933-9b10-52ffa9740042": "Thingy Quaternion Characteristic",
    "ef680406-9b35-4933-9b10-52ffa9740042": "Thingy Raw Data Characteristic",
    "ef680408-9b35-4933-9b10-52ffa9740042": "Thingy Rotation Characteristic",
    "ef680501-9b35-4933-9b10-52ffa9740042": "Thingy Sound Configuration Characteristic",
    "ef680502-9b35-4933-9b10-52ffa9740042": "Thingy Speaker Data Characteristic",
    "ef680503-9b35-4933-9b10-52ffa9740042": "Thingy Speaker Status Characteristic",
    "ef680402-9b35-4933-9b10-52ffa9740042": "Thingy Tap Characteristic",
    "ef680201-9b35-4933-9b10-52ffa9740042": "Thingy Temperature Characteristic",
    "ee0c2083-8786-40ba-ab96-99b91ac981d8": "Unlock",
    "e95db9fe-251d-470a-a062-fa1922dfa9a8": "micro:bit Pin IO Configuration",
    "e95d9250-251d-470a-a062-fa1922dfa9a8": "micro:bit Temperature",
    "be15beef-6186-407e-8381-0bd89c4d8df4": "Anki Drive Vehicle Service",
    "7905f431-b5ce-4e99-a40f-4b1e122d00d0": "Apple Notification Center Service",
    "d0611e78-bbb4-4591-a5f8-487910ae4366": "Apple Continuity Service",
    "8667556c-9a37-4c91-84ed-54ee27d90049": "Apple Continuity Characteristic",
    "9fa480e0-4967-4542-9390-d343dc5d04ae": "Apple Nearby Service",
    "af0badb1-5b99-43cd-917a-a77bc549e3cc": "Nearby Characteristic",
    "69d1d8f3-45e1-49a8-9821-9bbdfdaad9d9": "Control Point",
    "9fbf120d-6301-42d9-8c58-25e699a21dbd": "Notification Source",
    "89d3502b-0f36-433a-8ef4-c502ad55f8dc": "Apple Media Service",
    "9b3c81d8-57b1-4a8a-b8df-0e56f7ca51c2": "Remote Command",
    "2f7cabce-808d-411f-9a0c-bb92ba96c102": "Entity Update",
    "c6b2f38c-23ab-46d8-a6ab-a3a870bbd5d7": "Entity Attribute",
    "955a1523-0fe2-f5aa-a094-84b8d4f3e8ad": "Beacon Config",
    "a6c31337-6c07-453e-961a-d8a8a41bf368": "Candy Dispenser Service",
    "00001530-1212-efde-1523-785feabcd123": "Device Firmware Update Service",
    "88400001-e95a-844e-c53f-fbec32ed5e54": "Digital Bird Service",
    "ee0c2080-8786-40ba-ab96-99b91ac981d8": "Eddystone-URL Configuration Service",
    "8e400001-f315-4f60-9fb8-838830daea50": "Experimental Buttonless DFU Service",
    "00001523-1212-efde-1523-785feabcd123": "Nordic LED Button Service",
    "8d53dc1d-1db7-4cd3-868b-8a527460aa84": "SMP Service",
    "ef680100-9b35-4933-9b10-52ffa9740042": "Thingy Configuration Service",
    "ef680200-9b35-4933-9b10-52ffa9740042": "Thingy Environment Service",
    "ef680400-9b35-4933-9b10-52ffa9740042": "Thingy Motion Service",
    "ef680500-9b35-4933-9b10-52ffa9740042": "Thingy Sound Service",
    "ef680300-9b35-4933-9b10-52ffa9740042": "Thingy User Interface Service",
    "b35d7da6-eed4-4d59-8f89-f6573edea967": "URI Beacon Config (V1)",
}


def uuidstr_to_str(uuid_):
    uuid_ = uuid_.lower()
    s = uuid128_dict.get(uuid_)
    if s:
        return s

    if not s and uuid_.endswith("-0000-1000-8000-00805f9b34fb"):
        s = "Vendor specific"
    v = int(uuid_[:8], 16)
    if (v & 0xFFFF0000) == 0x0000:
        s = uuid16_dict.get(v & 0x0000FFFF, s)
    if not s:
        return "Unknown"

    return s


def register_uuids(uuids_to_descriptions: Dict[str, str]) -> None:
    """Add or modify the mapping of 128-bit UUIDs for services and characteristics to descriptions.

    Args:
        uuids_to_descriptions: A dictionary of new mappings

    """
    uuid128_dict.update(uuids_to_descriptions)

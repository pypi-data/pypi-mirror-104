# Factoring Total
[![PyPI version](https://badge.fury.io/py/FactoringRuc.svg)](https://pypi.org/project/FactoringRuc/1.0.0/)


## Descripción
Libreria para obtener datos basicos desde la SUNAT

## Instalación
```
pip install FactoringRuc
```

## Uso básico
```python
from factoring_ruc import ConsultaRuc


cr = ConsultaRuc()
usuario_enc = ""
password_enc = ""
key = ""
tipo = ""
ruc = ""
bloque = ""
respuesta = cr.search_by_document(usuario_enc,password_enc,key,tipo,ruc,bloque)
print(respuesta)
```

Obtendremos el siguiente resultado:

```python
{'informacion_basica': {'TDoc': 'R', 'NDoc': '20377892918', 'RelTDoc': '', 'RelNDoc': '', 'RazSoc': 'LEASING TOTAL S.A', 'NomCom': '-', 'TipCon': 'SOCIEDAD ANONIMA', 'IniAct': '1997-10-14', 'ActEco': '65912 - ARRENDAMIENTO CON OPCION DE COMPRA', 'FchInsRRPP': '1998-01-15', 'NumParReg': '-             ', 'Fol': '-    ', 'Asi': '-    ', 'AgeRet': 'S', 'ApeMat': '', 'ApePat': '', 'Nom': '', 'DigVer': '', 'Sex': '', 'FecNac': '', 'EstCon': 'ACTIVO', 'EstDom': 'HABIDO', 'EstDomic': '00', 'CondDomic': '00', 'Direcc': [{'Direccion': 'AVENIDA CIRCUNVALACION CLUB GOLF  NRO 134 SANTIAGO DE SURCO - LIMA - LIMA (TORRE 2 PISO 16)', 'Fuente': 'SUNAT - DOMICILIO FISCAL'}, {'Direccion': 'AVENIDA J PARDO  NRO. 231 MIRAFLORES - LIMA - LIMA (PISO 11 OFICINA 1101)', 'Fuente': 'SUNAT - OF.ADMINIST.'}], 'RepLeg': [{'TDOC': 'D', 'NDOC': '09377548', 'Nombre': 'RUIZ SANDOVAL SILVIA LILIANA', 'FecIniCar': '2013-01-22', 'Cargo': 'APODERADO'}, {'TDOC': 'D', 'NDOC': '30862793    ', 'Nombre': 'NUÑEZ MOLLEAPASA DAVID ANIBAL', 'FecIniCar': '1998-08-16', 'Cargo': 'GERENTE GRAL'}, {'TDOC': 'D', 'NDOC': '42848529', 'Nombre': 'ROSAS AVALOS AARON DIEGO', 'FecIniCar': '2013-07-04', 'Cargo': 'APODERADO'}]}}
```

## Configuración

Revisar PDF enviado

## Métodos

#### search_by_document(`usuario_enc, password_enc, key, tipo, ruc)
Con esto, obtendremos informacion basica del ruc o tipo de documento a consultar. Devolverá por defecto un diccionario ([https://docs.python.org/3.6/tutorial/datastructures.html#dictionaries](https://docs.python.org/3.6/tutorial/datastructures.html#dictionaries)).

## Consideraciones
* Debe utilizar python >=3.6


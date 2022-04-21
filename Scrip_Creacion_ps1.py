# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import sys

# print(sys.argv[0])
# print(sys.argv[1])
# print(sys.argv[2])
# print(sys.argv[3])
# print(sys.argv[4])
# print(sys.argv[5])
# print(sys.argv[6])
# print(sys.argv[7])
# print(sys.argv[8])
# print(sys.argv[9])
# print(sys.argv[10])
# print(sys.argv[11])

Nombre=sys.argv[1]
Apellido=sys.argv[2]
Usuario=sys.argv[3]
Grupo=sys.argv[4].replace("¾", "ó")
subGrupo=sys.argv[5]
Contrasena=sys.argv[6]

Grupo="Dirección de Crecimiento"
subGrupo="Proyectos Construcción"
sub_subGrupo="Ternium"

Cargo=sys.argv[7]
Office=sys.argv[8]
sub_subGrupo=sys.argv[9]


if len(sub_subGrupo) > 2:
    string_direccion='"OU='+sub_subGrupo+',OU='+subGrupo+',OU='+Grupo.replace("¾", "ó")
    
else:
    string_direccion='"OU='+subGrupo+',OU='+Grupo.replace("¾", "ó")



print(Nombre,Apellido,Usuario,Grupo,subGrupo,Contrasena,Cargo,Office)

with open(r'C:\Users\lambda.analytics\Desktop\Crear_Usuario.ps1', 'w') as f:
    f.write('\r\n')
    f.write('if (!([Security.Principal.WindowsPrincipal][Security.Principal.WindowsIdentity]::GetCurrent()).IsInRole([Security.Principal.WindowsBuiltInRole] "Administrator")) { Start-Process powershell.exe "-NoProfile -ExecutionPolicy Bypass -File `"$PSCommandPath`"" -Verb RunAs; exit }\r\n')
    f.write('$NewUserParameters = @{\r\n')
    f.write('"GivenName" = "'+Nombre+'"\r\n')
    f.write('"Surname" = "'+Apellido+'"\r\n')
    f.write('"Name" = "'+Nombre+' '+Apellido+'"\r\n')
    f.write('"DisplayName" ="'+Nombre+' '+Apellido+'"\r\n')
    f.write('"AccountPassword" = (ConvertTo-SecureString "'+Contrasena+'" -AsPlainText -Force)\r\n')
    f.write('"path"= '+string_direccion+',OU=Usuarios,DC=edemco,DC=local"\r\n')
    # f.write('"path"= "OU='+subGrupo+',OU='+Grupo.replace("¾", "ó")+',OU=Usuarios,DC=edemco,DC=local"\r\n')
    f.write('"UserPrincipalName"="'+Usuario+'@edemco.co"\r\n')
    f.write('"SamAccountName" ="'+Usuario+'"\r\n')    
    f.write('"email" = "'+Usuario+'@edemco.co"\r\n')
    f.write('"description" = "'+Cargo+'"\r\n')
    f.write('"OfficePhone" ="444-6500"\r\n')
    f.write('"HomePage" = "www.edemco.co"\r\n')
    f.write('"Organization" ="edemco"\r\n')
    f.write('"Title" = "'+Cargo+'"\r\n')
    f.write('"Department" ="EDEMCO"\r\n')    
    f.write('"Enabled" = $true}\r\n')
    f.write('New-AdUser @NewUserParameters\r\n')
    



with open(r'C:\Users\lambda.analytics\Desktop\Grupo_Usuario.ps1', 'w') as f:
    f.write('\r\n')
    f.write('if (!([Security.Principal.WindowsPrincipal][Security.Principal.WindowsIdentity]::GetCurrent()).IsInRole([Security.Principal.WindowsBuiltInRole] "Administrator")) { Start-Process powershell.exe "-NoProfile -ExecutionPolicy Bypass -File `"$PSCommandPath`"" -Verb RunAs; exit }\r\n')
    f.write('''$Direccion_Usuario=Get-ADUser -Filter 'Name -like "'''+Nombre+" "+Apellido+'''"'''"'| select DistinguishedName\r\n")
    f.write('Add-ADGroupMember -Identity "Navegacion_Restringido" -Members $Direccion_Usuario\r\n')
    f.write('Add-ADGroupMember -Identity "VPN_Forti" -Members $Direccion_Usuario\r\n')
    f.write('Add-ADGroupMember -Identity "Usuarios TS" -Members $Direccion_Usuario\r\n')    
    f.write('Add-ADGroupMember -Identity "Office 365" -Members $Direccion_Usuario\r\n')    

    if Office == "NivelBasico":
        f.write('Add-ADGroupMember -Identity "NivelBasico" -Members $Direccion_Usuario\r\n')   
    elif Office == "NivelMedio":
        f.write('Add-ADGroupMember -Identity "NivelMedio" -Members $Direccion_Usuario\r\n')   
    elif Office == "NivelAlto":
        f.write('Add-ADGroupMember -Identity "NivelAlto" -Members $Direccion_Usuario\r\n')   
    else:
        print("Sin nivel office")
        
    
    

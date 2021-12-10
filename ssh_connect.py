import paramiko
import select
import xarray as xr
import os
from netCDF4 import Dataset

jumpbox_public_addr = 'airchem.snu.ac.kr'
jumpbox_private_addr = 'airchem.snu.ac.kr'
target_addr = 'scherzo.snu.ac.kr'

jumpbox=paramiko.SSHClient()
jumpbox.set_missing_host_key_policy(paramiko.AutoAddPolicy())
jumpbox.connect(jumpbox_public_addr, username='intern', password='acmgmodeling')

jumpbox_transport = jumpbox.get_transport()
src_addr = (jumpbox_private_addr, 22)
dest_addr = (target_addr, 22)
jumpbox_channel = jumpbox_transport.open_channel("direct-tcpip", dest_addr, src_addr)

target=paramiko.SSHClient()
target.set_missing_host_key_policy(paramiko.AutoAddPolicy())
target.connect(target_addr, username='intern01', password='acmgmodeling', sock=jumpbox_channel)

sftp = target.open_sftp()
file = sftp.open('/veloce2/sel/GC13.0.0/OutputDir/gems_apriori_0.25x0.3125/GEOSChem.AerosolMass.20200701_0000z.nc4',bufsize=32768)
file.prefetch()
print('start read')
b = file.read()

nc = Dataset('test.nc', memory=b)
print(nc)
target.close()
jumpbox.close()
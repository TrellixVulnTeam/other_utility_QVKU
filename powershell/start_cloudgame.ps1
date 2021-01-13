
$version_path = "HKLM:\SOFTWARE\CloudGame"
$version_name = "VersionString"
$path_prefix = "win32.release.crservice_"
$app = "host_service.exe"

$reg_version = Get-ItemPropertyValue -Path $version_path -Name $version_name

$dir_path = $path_prefix+$reg_version

$full_path = "D:\"+ $dir_path +"\" + $dir_path + "\" + $app


Start-Process $full_path
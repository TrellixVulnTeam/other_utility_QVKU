
if test ${#} -lt 1 ; then
    echo 'error: input t or p'
    exit
fi

testenv='true'
if test ${1} = p ; then
testenv='false'
fi

file='/f/program files (x86)/hycgclient/HYCGClient/Client/hycgconfig.json'

sed -i "s/test_env\":.*,/test_env\":${testenv},/g" "${file}"

echo "change to ${1}"


taskkill //F //T //IM HYCloudPlay.exe


cd "/f/program files (x86)/hycgclient/HYCGClient/Client"

start HYCloudPlay.exe
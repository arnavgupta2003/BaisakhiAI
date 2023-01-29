async function sendTransaction(){
    let param =  [
        {
        "from": '0x552103E85b9b56D28b5E3bf6c61e59C9F03b01b9',
        "to": '0xdc4583D5Bb820E2477648AbbB075060F76A8267e',
        "gas": Number(2100).toString(16), // 30400
        "gasPrice": Number(2500).toString(16), // 10000000000000
        "value": '0x9184e72a', // 2441406250 
    },
    ]
    let result  = await window.ethereum.request({method:"eth_sendTransaction",param}).catch((err)=>{
        console.log(err);
    })

}



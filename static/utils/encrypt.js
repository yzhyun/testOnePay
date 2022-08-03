function getEncSignature(trgtStr){
  console.log("crypto-js 진입");
  
  encSignature = CryptoJS.SHA256(trgtStr)
  hexString = CryptoJS.enc.Hex.stringify(encSignature);
  
  return hexString;
}


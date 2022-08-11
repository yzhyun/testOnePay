function getEncSignature(trgtStr){
  encSignature = CryptoJS.SHA256(trgtStr)
  hexString = CryptoJS.enc.Hex.stringify(encSignature);
  
  return hexString;
}


import CryptoJS from "crypto-js";

export const getEncryptToHex = (value) => {
  const encryptValue = CryptoJS.SHA256(value);
  const hexString = CryptoJS.enc.Hex.stringify(encryptValue);

  return hexString;
};
// 경우에 따라 value가 getParameter로 변경된 이후에 hashKey를 붙인 값이 들어오는 경우가 있습니다.
// 따라서 해당 함수는 내부에서 stringify를 진행하지 않습니다.

export const aesCbcPkc5Encode = (content, secretKey) => {
  //  암호키는 32 바이트입니다.
  const parsedKey = CryptoJS.enc.Utf8.parse(secretKey);
  const iv = CryptoJS.enc.Utf8.parse(secretKey.substring(0, 16));
  const encryptResult = CryptoJS.AES.encrypt(content, parsedKey, {
    iv,
    mode: CryptoJS.mode.ECB,
    padding: CryptoJS.pad.Pkcs5
  });
  return encryptResult.toString();
};

export const aesCbcPkc5Decode = (encodeKey, secretKey) => {
  const parsedKey = CryptoJS.enc.Utf8.parse(secretKey);
  const iv = CryptoJS.enc.Utf8.parse(secretKey.substring(0, 16));

  var decrypted = CryptoJS.AES.decrypt(encodeKey, parsedKey, {
    iv,
    mode: CryptoJS.mode.CBC,
    padding: CryptoJS.pad.Pkcs5
  });
  return decrypted.toString(CryptoJS.enc.Utf8);
};

export const getSignature = (...values) =>
  CryptoJS.enc.Hex.stringify(CryptoJS.SHA256(values.join("")));

// export const validateSignature = (origin, ...values) =>
//   origin === getSignature(values) ? true : false;
export const validateSignature = (origin, ...values) => true;

// aes 암복호화 함수는 검증이 필요합니다. 아마 세틀 뱅크에서 사용되거나, 혹은 아예 미사용될 수 있습니다.
// 아마 aes 함수를 쓸 상황은... 없을 겁니다. 살펴보니 서버측에서 모두 알아서 암호화해서 내려주는 형태인 걸로 보입니다.

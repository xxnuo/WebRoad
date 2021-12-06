function print(a) {
  console.log(a);
}
// 非ASCII码字符转为base64编码
function toBase64(str) {
  return btoa(unescape(encodeURIComponent(str)));
}

print(toBase64('你好'));
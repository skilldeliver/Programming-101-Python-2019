# Break the Cipher (bonus task)


The `secret_keeper.py` file has 1 public function - `make_it_secret('publicmessage')`
It accepts a public message and gives a secret one.

So in order to decrypt some message you need to generate all combinations and encrypt them with this function and then compare the encrypted values. If they are equal you've successfully decrypted the message.

Example:

```
>>> make_it_secret('publicword')
'0da537d4cad7299cbbd9905932463537'

# Our encrypted message is not '0da537d4cad7299cbbd9905932463537'

>>> make_it_secret('not_successful_attempt') == '0da537d4cad7299cbbd9905932463537'
False


>>> make_it_secret('publicword') == '0da537d4cad7299cbbd9905932463537'
True

# You decrypted the message
```

## Task

Your task is simple - *decrypt the following message*:

```
8021f7e4b05dada0ad3d47567e52249e 6864f389d9876436bc8778ff071d1b6c a4757d7419ff3b48e92e90596f0e7548
cae8d14edd025e72c59dbab6f378c95a d78b6f30225cdc811adfe8d4e7c9fd34 b5f3729e5418905ad2b21ce186b1c01d ab86a1e1ef70dff97959067b723c5c24
7e1321b3c8423b30c1cb077a2e3ac4f0 4015e9ce43edfb0668ddaa973ebc7e87 03d59e663c1af9ac33a9949d1193505a a80698366d88c5ebf1357689cc3ca8fe 1952a01898073d1e561b9b4f2e42cbd7 c5af0543407a6e8ba11db6a69f792014 c67fd61e3b7d35f07e3ca92c8a84a5ab 6c92285fa6d3e827b198d120ea3ac674
1666ca77ab75f7d731e645fa6ef4fc60 4ad44a676546464b2c4b8c9e4529bdf0 d4408643ccbd7e83d0c54f42e405d618
90f910a44798e0d68879b43382042a40 0b3b8343a911a6327e7f3d8038fd58a6
dd7536794b63bf90eccfd37f9b147d7f 92159805cf28ee78e13c41ebbbb1aeb4 639bae9ac6b3e1a84cebb7b403297b79 0cc175b9c0f1b6a831c399e269772661 3e1867f5aee83045775fbe355e6a3ce1
```

## Limitations:

1. The maximum length of each word is **5 symbols**. 
2. Allowed characters
  - lowercased letters - `a-z`
  - uppercased letters - `A-Z`
  - digits - `0-9`


## Requirements:

1. Create a database table `CipherBreaker` with the following columns:

  - `id` - primary key, not null, unique, auto increment
  - `message` - text (this is the public message)
  - `encrypted_message` - text (this is the public message **after** you call `make_it_secret`)

2. After you try a new string you should store it into the `CipherBreaker` table

3. When you try to decrypt a new value (like '0da537d4cad7299cbbd9905932463537') you should first check in `CipherBreaker` if you've already decrypted it ;). That's why you need **step 2**

4. If stop the program while running(kill the process) and then run it again it should continue decrypting from the same place (and not from the beginning)


**Here's the deal:** If you send the decrypted message with a working solution(see the requirements), you'll get a beer at the end of the course. Deal ?

NOTE: The encryption will take some time. If you make a working solution (if it starts decrypting the message and meets the requirements), you'll get a beer anyway :)

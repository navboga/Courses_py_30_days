import string
import random
import base64
print(random.choice(string.ascii_lowercase))
encode =("UEsDBBQACAAIAHl+Mk8AAAAAAAAAAAAAAAAHAAAAeHh4LnR4dK1U246bMBB9369AvOQp+IINNhBWURr1JduNNqnUN0SJk0UNFxmz2fx9bXKBRGmlSkUG7Jk5njPHA9HzZ7G3PoRs8qq0JtYIOXBkiTKrNnm5M4ZWbcds9Bw/RVlV1KkUyzT7JZSlcWUTfDb5xH5Xqg4AOBwOzsF1KrkDGEIEfrwsVtm7KNJxXjYqLTNhWzo+aDrjospSpZNe4SezU6jGkS2Yr5ZLMN2JUi3TY6FfDXgTu7xRMhdmmlVllu/zbgvwQRMILQNJbiBJD0luIUkHcT6bjTW8/kxlVkmhH7oQmeaGzSCn8SUDX7+5fZZJNHU9zvqIvxX9ONN5p/+mlm3lm4mNIfN816cYQzt+0gJETVsUqTx2C7PWSM0jUzHnkEB9eTwCV2MfdWoNIfNqc7Eax1ZWRYwh8scQjxFdIy8gLCA0Ap1nEKmqmzg/0IO4EdD2SxbwMI1GqnQ/Laq2VK/bS/0xNtBHjivnVkrd6MeuJ9WxFhP7/piC2fe3ZFuoBCI7ZghqBmfQbfJVW8SUYgfCc1JjuIn4In6qmBLi4AuvztJJDoaaR/U9z7o7KU0AY48yhCAO9c0p4z7z9XcWGtkgRhR5hBGqjyhEzPc4YpC7DIfzxVyP2erbfO0g7BLq+SHhJg4atJ4SzsPpbJa8fF2vQmTKCHWxoX+aR6C+44LvuXgQYcL4kIuPfOL2XDhkzOP/yoUSeCGDcUhd3MlXn2Xrleo7o/s3xb8BUEsHCDJ0ZRsnAgAA1gQAAFBLAQIUABQACAAIAHl+Mk8ydGUbJwIAANYEAAAHAAAABwAAAAAAAAAAAAAAAAB4eHgudHh0Y29tbWVudFBLBQYAAAAAAQABADwAAABcAgAA AAA=")
data = base64.decode(encode)
print(data)
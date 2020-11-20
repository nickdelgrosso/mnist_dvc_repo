

## DVC Files

`.dvc` files are added to git, and they store the current hash and reference to the data.

Reference: https://dvc.org/doc/user-guide/dvc-files-and-directories


### Calculating Hashes

MD5 Hash: 
Linux/Mac/GitBash:  `md5sum <filename>`
Windows: `CertUtil -hashfile <filename> MD5`
Python: `from hashlib import md5; md5(<bytedata>).hexdigest()`



## DVC Remotes

DVC remotes are the location of a DVC project's databases.  Lots of different cloud services are supported; the full list and how to work with them can be found here:  https://dvc.org/doc/command-reference/remote/add

There's a lso a useful table for reference here: https://dvc.org/doc/command-reference/import-url

### Google Drive

Google Drive is the simplest to set up, and works great for some projects.  DVC's documentation focuses on google drive (with the most extensive docs for it: https://dvc.org/doc/user-guide/setup-google-drive-remote), so let's take a look at that first.

`dvc remote add <name> gdrive://<folder-id-here>`


### Local Remote

Any location on your computer can be used as a remote.  It's not terribly useful for sharing data between people, but works great for local testing and version control.

`dvc remote add <name> <path>`

### SSH Remote

SSH is a nice general-purpose sharing techniqe that works great in small teams and companies, where a server is already there.  Here, we'll use Linode 
to try out an SSH remote

`dvc remote add <name> ssh://<ip>/<path>`

Credentials are added in subsequent commands:
```
dvc remote modify <name> user <username>
dvc remote modify <name> port <port>
dvc remote modify --local <name> password <password>
```

A thread on this topic can be found here: https://discuss.dvc.org/t/how-do-i-use-dvc-with-ssh-remote/279



## References

  - Downloading MNIST data with Keras: https://machinelearningmastery.com/how-to-develop-a-convolutional-neural-network-from-scratch-for-mnist-handwritten-digit-classification/

  - 
[![Run on Repl.it](https://repl.it/badge/github/nickdelgrosso/mnist_dvc_repo)](https://repl.it/github/nickdelgrosso/mnist_dvc_repo)


# Exploring DVC with the MNIST dataset

[DVC](https://dvc.org/) is a very useful command-line tool that helps keep code and data versioned together.  Rather than trying to replace git, it works with git to keep track of which versions of datasets were present alongside which versions of code.  It does this using a stubfile strategy similar to [git-annex](https://git-annex.branchable.com/).  

DVC also has some basic pipelining mechanisms which can be used to track which scripts produce which datasets.  This repo contains some useful data, and will serve as a playground repository for exploring file management with DVC.


The full list of DVC commands: https://dvc.org/doc/command-reference


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

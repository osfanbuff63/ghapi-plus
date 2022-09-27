# ghapi-plus

## About

This is a project to make a CLI and GUI interface around [`ghapi`](https://ghapi.fast.ai/).

### Why make another CLI interface?

I am fully aware that `ghapi` [includes a CLI interface](https://ghapi.fast.ai/cli.html). However, there's quite a few issues with it, which I will go into more detail in below:

- The CLI interface is confusing, and
- It uses 3 separate commands on the command line

#### The CLI interface is confusing

`ghapi`'s CLI interface requires you to put everything in Python-like parameters. To do basic things in the API that may or may not be possible in a way that is more user-friendly with [`gh`](https://cli.github.com). There's a huge missed opportunity for `ghapi` here, and my goal is to fill the gap.

#### It uses 3 separate commands on the command line

And just when you thought it couldn't get any worse, it turns out `ghapi` isn't just `ghapi`, but it's `ghpath` and `ghraw` as well, and they are all handled by the same code. Not only does this cause confusion, it's just weird when subcommands exist and are widely used, as well as parameters, which can be implemented in raw Python with `sys.argv`.

### What about the main ghapi_plus folder?

This folder is for a library wrapping around `ghapi` to make it simpler to implement into applications. However, the current version of the CLI and GUI use raw `ghapi`, and that will continue until the library is ready.

## Licensing

The entirety of the ghapi_plus directory, which will provide a wrapper for `ghapi`, is licensed under the Apache License 2.0; see [licenses/Apache-2.0.md](/licenses/Apache-2.0.md) for details.

Everything else, unless explicitly stated otherwise, is licensed under the GNU General Public License version 3 (or at your option, any later version), including the end product as a whole; see [licenses/GPL.md](/licenses/GPL.md) for details.

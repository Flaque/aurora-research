# Sea-floor

When we explored building an Electron project with React we noticed that it was incredibly difficult and frustrating. To do it yourself, with all the nicities of a good dev environment, requires a lot of work and complexity. If you choose to use a boilerplate, you end up with a project that is already massive and requires a fair amount of maintenance before we've even written a single line of code. 

The most widely used boilerplate project: [electron-react-boilerplate](https://github.com/chentsulin/electron-react-boilerplate) has 6 different webpack configuration files. It also presuposes linting and typing preferences. It adds plenty of code that must be removed. If you need to change anything about it, it's fairly difficult and because of the vast amount of libraries and tools it uses by default.

So instead, we built something called `sea-floor`. Sea-floor is a platform that you can build electron apps with react on top of. It handles all the compiling and configuration for you and picks smart defaults. With Sea-floor, your entire electron code can be just three lines of code:

``` js
import Sea from 'sea-floor';
import path from 'path';

Sea.open(path.resolve(__dirname, "./path/to/react/component.js"));
```

Compare that to the thousands of lines in the "blank" app from the boilerplate. 

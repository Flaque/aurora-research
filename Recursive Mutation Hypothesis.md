# Recursive Mutation Hypothesis

This doc describes a potential hypothesis of how mutations should be able to modify and change Aurora. If successful, this serves as a framework that can set the possible boundaries of the design process.

## Overview
A "recursive mutation" is an extension that can edit, delete, and add to an existing extension. This means that if Joe adds a mutation that gives a status bar, Sally can write a mutation for Joe's mutation that adds a "hide" button. 

In traditional extensibility models, users can only add onto the existing application. In this extensibility model, a user can remove features and edit existing ones as well. They also can add onto other people's applications.

This means that Aurora can branch off from a single root node and become wildly different applications depending on user's desires. 

## Major Assumptions Made

### We're continuing to use Electron or some other web platform. 
I assume this because it's fairly difficult to have complete extensibility in other platforms. The web is by far the easiest to do customizations and it also uses widely known and easily picked up languages. 

### We are using React or some other virtual DOM or tree system. 
The main reason I assume this is just practicality. We've already started learning this system and unless anyone's found any major flaws with it, I'm going to assume we'll continue working with it. 

### People want customizability
We assume this because there is a wide array of note taking applications out there with lots of variations, which implies that users are extremely diverse. However, given our conversations with users and our own experience, every app seems to be "wrong in different ways." In other words, there's no single app that is one-size-fits all.

### Some part of the user base will create extensions eventually assuming we give them adequate support
We assume this because it's happened with several other apps across different platforms, such as Atom and Sketch. 

## Possibilities of Mutations (and Proof of Concepts) 
These are things we know we can do with existing mutations. They're not an extensive list, but they help define the realm of possible (which is pretty big). 

### Mutations can turn off any component 
Proof of concept in React style API's using [HOC's](https://reactjs.org/docs/higher-order-components.html). 

``` js 
function turnOff(Component) {
	return class extends React.Component {
		render() {
			return false;
		}
	}
}
```

### Mutations can add to an existing component
Proof of concept in React style API's using [HOC's](https://reactjs.org/docs/higher-order-components.html). 

``` js
function extendExisting(Component) {
	return class extends React.Component {
		onClick() {
			// now I do something when clicked!
		}
	
		render() {
			return <Component onClick={this.doSomethingExtra} />
		}
	}
}
```

#### Adding another component

``` js
function extendExisting(Component) {
	return class extends React.Component {
		render() {
			return [ 
				<Component />, 
				<MyNewThing />
			];
		}
	}
}
```


### Mutations can edit an existing component 

Proof of concept in React style API's using [HOC's](https://reactjs.org/docs/higher-order-components.html). 

``` js
function extendExisting(Component) {
	return class extends React.Component {
		render() {
			return <SomeDifferentThing />
		}
	}
}
```

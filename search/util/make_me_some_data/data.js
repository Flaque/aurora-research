const faker = require("faker");
const _ = require("lodash");

const MAX_TAGS = 20;
const MAX_PARAGRAPH_WORDS = 1000;

// One off for creating parts of text or tags
const paragraph = () =>
  faker.random.words(faker.random.number(MAX_PARAGRAPH_WORDS));
const tag = words => faker.random.arrayElement(words.split(" "));

// Text component
const text = () => {
  return paragraph();
};

// Tags component
const tags = words => {
  const numTags = faker.random.number(MAX_TAGS);
  return _.range(numTags).map(() => tag(words));
};

// UUID component
const uuid = () => {
  return faker.random.uuid();
};

// Create a single random note
const note = () => {
  const _uuid = uuid();
  const _text = text();
  const _tags = tags(_text);

  return {
    uuid: _uuid,
    text: _text,
    tags: _tags
  };
};

/**
 * Creates `num` amounts of notes in the standard data format.
 * @param {int} num 
 */
const data = num => {
  return _.range(num).map(note);
};

module.exports = data;

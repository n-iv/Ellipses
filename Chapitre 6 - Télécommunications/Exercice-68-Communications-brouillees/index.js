const nodemailer = require('nodemailer');
const directTransport = require('nodemailer-direct-transport');

const fromHost = `nodemailer-direct-transport.${process.env.REPL_OWNER.toLowerCase()}.repl.co`;
const from = 'mail' + '@' + fromHost;

console.log('Email will be sent from', from, '\n');

const to = prompt('Who do you want to email? ');
const subject = prompt('Subject?                  ') || 'Send email test';
const html = prompt('Email body (accepts HTML) ') || '<h1>Send mail test</h1><p>(this is HTML)</p>';

const transport = nodemailer.createTransport(directTransport({
  name: fromHost
}));

transport.sendMail({
  from, to,
  subject,
  html
}, (err, data) => {
  if (err) {
    console.error('There was an error:', err);
  } else {
    console.log('Message sent successfully:', data);
  }
});
import dotenv from 'dotenv';
import nodemailer from 'nodemailer';

dotenv.config();

const transporter = nodemailer.createTransport({
	service: 'gmail',
	auth: {
		user: process.env.EMAIL,
		pass: process.env.PASSWORD
	}
});

const mailOptions = {
	from: process.env.EMAIL,
	to: 'shohruhwebdev@gmail.com',
	subject: 'Sending Email using Node.js',
	text: 'That was easy!'
};

transporter.sendMail(mailOptions, (error, info) => {
	if (error) {
		console.log(error);
	} else {
		console.log('Email sent: ' + info.response);
	}
});

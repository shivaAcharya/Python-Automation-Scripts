#! python3
# mclip.py - A multi-clipboard program.

TEXT = {'Busy': '''Can we do that later this week or next week''',
        'Upsell': '''Are you willing to make that donation every month?''',
        'Thankyou' : '''Hi ...,

I would like to thank you for taking the time to talk to me today. I really enjoyed our conversation and I learned a lot about the company culture and the position.

I am very interested in this role and would love to be considered for next steps.

Thank you again for your time and consideration.

Best Regards,
Shiva''',
        'Interview' : '''Hi ..........,

Thank you for reaching out to me. I am thrilled to receive this opportunity.

You can call me at 505-492-8001 so that I can share my background and career interests with you. Meanwhile, I can learn more about your company and the position.

I am available to chat during the following times:

   10/7 (Mon): 9 am to 3 pm
   10/8 (Tue): 11 am to 2 pm
   10/9 (Wed): 9 am to 1 pm
   10/10(Thu): 10 am to 4 pm
   10/11(Fri): 11 am to 1 pm     PT

Let me know what time works best for you, so we can schedule a phone conversation.

Thank you again!

Best Regards,
Shiva Acharya''',
        'Nooffer' : '''Dear ,

Thank you for getting back to me. While I'm disappointed to hear that I wasn't selected to move forward for the .............. position, I greatly appreciate the opportunity to interview
for the position and connect with Nami. I thoroughly enjoyed learning more about ............. and would love to be considered for any future job openings that closely match my
skillsets.

Meanwhile, I would love to connect with you on LinkedIn so that we can keep in touch and I can receive more updates on the company moving forward. I have sent you a connection invitation and hope you
will accept the request.

Thank you again for your time and consideration, ........ I hope our paths cross again, and I wish you and the rest of the team at ........ all the best for future endeavors.

Sincerely,
Shiva Acharya'''}

import sys, pyperclip

if len(sys.argv) < 2:
    print('Usage: py mclip.py[keyphrase] - copy phrase text')
    sys.exit()

keyphrase = sys.argv[1]

if keyphrase in TEXT:
    pyperclip.copy(TEXT[keyphrase])
    print('Text for ' + keyphrase + ' copied to clipboard.')
else:
    print('There is no text for' + keyphrase)

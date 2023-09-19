import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

def email_results(week_penalties, email_address, week):
    html_info = build_html(week_penalties)
    # send emails
    message = Mail(
        from_email = 'jrdnwilkin+dynasty@gmail.com',
        to_emails = email_address,
        subject = "Sleeper Dynasty 0 Point Starter Penalties - Week {}".format(week),
        html_content = html_info)
    try:
        sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
        response = sg.send(message)
        print(response.status_code)
        print(response.body)
        print(response.headers)
    except Exception as e:
        print(e)

def build_html(penalty_lists):
    html = '<p>'
    for username, penalty in penalty_lists.items():
        penalty_pluralized = 'penalty' if penalty['number'] == 1 else 'penalties'
        html += 'Player: {} had {} {}'.format(username, penalty['number'], penalty_pluralized)
        if penalty['number'] > 0:
            html += ' caused by: {}'.format(penalty['penalized_players'])
        html += '<br>'

    html += '</p>'
    return html


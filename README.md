# Kameti Tracker

A mobile-friendly tracker for managing a rotating committee: members, contribution rounds, payment status, payout order, and reminders. The interface supports English and Urdu, with English, Roman Urdu, and Urdu message templates.

**Live app:** [kameti-tracker.vercel.app](https://kameti-tracker.vercel.app/)

## Features

- Record paid, partial, and unpaid contributions, with cash or transfer methods and notes.
- See round totals, collection progress, due dates, and the current payout recipient.
- Send prefilled reminders and receipts through WhatsApp or SMS.
- Draw or adjust payout order and review its change history.
- Export records to CSV, print a statement, and back up or restore tracker data.
- Sign in from multiple devices and sync the account's tracker through Supabase.

## Requirements

- Python 3.8 or later
- A Supabase project configured for email and password authentication
- Internet access in the browser for Supabase and hosted frontend assets

## Setup

1. Create a Supabase project. In its SQL Editor, run [`supabase/schema.sql`](supabase/schema.sql). Enable email/password sign-in in Authentication settings.
2. Set the Supabase Site URL to `http://localhost:8000` and add `http://localhost:8000/**` to the redirect URL allow list. Add your deployed origin there if you later host the app.
3. Create or edit a `.env` file in the project root with your project URL and **publishable** key:

   ```dotenv
   SUPABASE_URL=https://your-project-ref.supabase.co
   SUPABASE_PUBLISHABLE_KEY=sb_publishable_your_key
   ```

4. Install the Python dependency and start the local server from this folder:

   ```powershell
   python -m pip install -r requirements.txt
   python server.py
   ```

5. Open [http://localhost:8000/Kameti%20Tracker%20(MVP).html](http://localhost:8000/Kameti%20Tracker%20(MVP).html), then create an account or sign in. Confirm your email first if email confirmation is enabled.

The Flask app reads `.env` locally and exposes only the project URL and publishable key to the browser through `/config.js`. The publishable key is public by design; never use or expose a Supabase `service_role` key in this app. `.env` is ignored by Git.

## Deploy to Vercel

Import this repository as a Vercel project and use the Python/Flask runtime. In **Project Settings → Environment Variables**, add `SUPABASE_URL` and `SUPABASE_PUBLISHABLE_KEY` for Production (and Preview if you use preview deployments). Deploy or redeploy after saving the variables. Set the Supabase Site URL to your production domain and add it to the redirect URL allow list.

Vercel loads the top-level Flask `app` in `server.py`; `/config.js` reads the Vercel environment variables at runtime. Do not upload `.env` to the repository.

## Data and Privacy

Each authenticated Supabase account has its own tracker row in `public.kameti_trackers`. Row-level security limits access to that account's row. Changes are cached in the browser and synced shortly afterward. On first sign-in, existing local tracker data is imported when the account has no cloud record.

Use the **Backup** view to export or restore tracker JSON. The optional four-digit PIN is a casual in-app lock, not encryption. Keep your Supabase project secure and use its backup options.

## Project Files

- `Kameti Tracker (MVP).html`: application UI and client-side tracker logic
- `server.py`: Flask app, local server, and environment-backed `/config.js` endpoint
- `requirements.txt`: Python server dependencies
- `supabase/schema.sql`: tracker table, grants, and row-level security policies
- `SUPABASE_SETUP.md`: detailed Supabase setup and existing-data migration notes

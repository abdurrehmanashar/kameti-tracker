create table if not exists public.kameti_trackers (
  user_id uuid primary key references auth.users (id) on delete cascade,
  data jsonb not null default '{}'::jsonb,
  updated_at timestamptz not null default now()
);

alter table public.kameti_trackers enable row level security;

drop policy if exists "Users can read their own tracker" on public.kameti_trackers;
create policy "Users can read their own tracker"
  on public.kameti_trackers
  for select
  to authenticated
  using ((select auth.uid()) = user_id);

drop policy if exists "Users can create their own tracker" on public.kameti_trackers;
create policy "Users can create their own tracker"
  on public.kameti_trackers
  for insert
  to authenticated
  with check ((select auth.uid()) = user_id);

drop policy if exists "Users can update their own tracker" on public.kameti_trackers;
create policy "Users can update their own tracker"
  on public.kameti_trackers
  for update
  to authenticated
  using ((select auth.uid()) = user_id)
  with check ((select auth.uid()) = user_id);

grant select, insert, update on public.kameti_trackers to authenticated;

import { papi } from '$utils/api';
import { getUser } from '$utils/auth';
import { redirect } from '@sveltejs/kit'

export async function handle({ event, resolve }) {
      // get cookies from browser
      // todo, get user from cookies
      //event.locals.user = await getUserInformation(event.cookies.get('sessionid'));
      event.locals.user = getUser(event.cookies);

      // if (!event.locals.user) {
      //   const authToken = event.cookies.get('Authorization')
        
      //   if (authToken) {
      //     // get user from endpoint
      //     try{
      //       const response = await papi(event.fetch, "auth/current");
      //       const user = await response.json()
      //       if (user) {
      //         console.log(event.locals.user, "overwrite")
      //         event.locals.user = user
      //       }
      //     } catch {
      //       console.log("here")
      //     }
      //   }
      // }

      if (event.url.pathname.startsWith("/profile")) {
        if (!event.locals.user){
          throw redirect(303, "/")
        }
      }
      if (event.url.pathname.startsWith("/admin")) {
        if (!event.locals.user){
          throw redirect(303, "/")
        }
      }

      // console.log('Server Hook:', event.url.href);
      // console.log("href", event.url.pathname)

      // if (event.url.pathname.startsWith('/private')) {
      //   return await event.fetch(`${event.url.href.replace("/private", "/api")}`);
      // }

      // if (!event.locals.obj && event.url.pathname.startsWith('/api')) {
      //   try {
      //     const objResp = await event.fetch('/api/endpoint');
      //     if (!objResp.ok) throw objResp;
      //     event.locals.obj = await objResp.json();
      //   } catch {
      //     event.locals.obj = null;
      //   }
      // }
  
    return await resolve(event)
  }

export async function handleFetch({ request, fetch, event }) {

    request.headers.set('Authorization', `${event.cookies.get('Authorization')}`);
    let x = await fetch(request);
    return x;
}

// export function handleError({ error, event }) {

//   console.log("ERROR", error)
//   return {
//       message: 'Whoops!',
//       // code: error?.code ?? 'UNKNOWN',
//       error: error
//   };
// }
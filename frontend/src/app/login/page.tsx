import { login, signup } from './actions'
import Image from "next/image";
import { Button } from "@/components/ui/button"
import { Input } from "@/components/ui/input"

export default function LoginPage() {
  return (
    <main className="flex min-h-screen flex-col p-10 bg-gradient-to-r from-purple-100 dark:from-purple-500 to-violet-300">

      <div className="flex m-20 min-w-screen justify-center">
          <Image
            src="/ull_logo.png"
            alt="Logo ULL"
            width={300}
            height={100}
            priority
          />
        </div>

      <div className="flex w-full justify-center">
        <form className="flex flex-col basis-3/4 bg-violet-100 rounded-xl border border-purple-300">
          <div  className="space-y-4 p-5">
            <div className="grid">
              <Input id="email" name="email" type="email" placeholder="Email" required/>
            </div>

            <div className="grid">
              <Input id="password" name="password" type="password" placeholder="Contraseña" required/>
            </div>
          </div>
          
          <div className="grid p-5">
            <Button formAction={login}>Log in</Button>
          </div>

        </form>
        
      </div>
    </main>
  )
}
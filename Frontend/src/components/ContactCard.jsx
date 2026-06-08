import { FaLinkedin, FaEnvelope } from "react-icons/fa";

export default function ContactCard({ contact }) {
  return (
    <div
      className="
        bg-slate-900
        border
        border-slate-800
        rounded-2xl
        p-5
        hover:border-violet-500
        transition
      "
    >
      <div
        className="
    w-12
    h-12
    rounded-full
    bg-violet-600
    flex
    items-center
    justify-center
    font-bold
    mb-4
  "
      >
        {contact.name?.charAt(0)}
      </div>
      <h3 className="text-xl font-semibold">{contact.name}</h3>

      <p className="text-violet-400 mt-1">{contact.title}</p>

      <p className="text-slate-400 mt-2">{contact.company}</p>

      <div className="mt-4 space-y-2">
        {contact.email && (
          <a
            href={`mailto:${contact.email}`}
            className="
              flex
              items-center
              gap-2
              text-slate-300
              hover:text-white
            "
          >
            <FaEnvelope />
            {contact.email}
          </a>
        )}

        {contact.linkedin_url && (
          <a
            href={contact.linkedin_url}
            target="_blank"
            rel="noreferrer"
            className="
              flex
              items-center
              gap-2
              text-blue-400
              hover:underline
            "
          >
            <FaLinkedin />
            LinkedIn Profile
          </a>
        )}
      </div>
    </div>
  );
}

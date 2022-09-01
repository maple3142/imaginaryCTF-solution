import type { GetStaticPaths, GetStaticProps } from "next";
import { join } from "path";
import fs from "fs";
import matter from "gray-matter";
import PostBody from "../../components/post-body";
import markdownToHtml from "../../lib/markdownToHtml";

interface PostProps {
  title: string;
  content: string;
  isProtected: boolean;
}

const postsDirectory = join(process.cwd(), "_posts");

const Protected = ({ content }: PostProps) => {
  return <PostBody content={content} />;
};

Protected.requireAuth = true;

export const getStaticPaths: GetStaticPaths = async () => {
  const files = fs.readdirSync(postsDirectory);

  const postPaths = files
    .map((path) => {
      const fileContents = fs.readFileSync(join(process.cwd(), "_posts", path));
      const { data } = matter(fileContents);

      return {
        path: path,
        isProtected: data["protected"],
      };
    })
    .filter(({ isProtected }) => isProtected)
    .map(({ path }) => {
      return {
        params: {
          post: path.replace(/\.md$/, ""),
        },
      };
    });

  return {
    paths: postPaths,
    fallback: false,
  };
};

export const getStaticProps: GetStaticProps<PostProps> = async (context) => {
  const post = context.params?.post?.toString();

  if (!post) {
    return {
      notFound: true,
    };
  }

  const path = join(process.cwd(), "_posts", post);
  const fileContents = fs.readFileSync(`${path}.md`);

  const { data, content } = matter(fileContents);

  return {
    props: {
      title: data["title"],
      content: await markdownToHtml(content),
      isProtected: data["protected"],
    },
  };
};

export default Protected;

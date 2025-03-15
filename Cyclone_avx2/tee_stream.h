// tee_stream.h - A header file that contains the definition of the TeeBuf class.
// Coded by @B0dre
#include <streambuf>
#include <ostream>

class TeeBuf : public std::streambuf {
    std::streambuf *sb1;
    std::streambuf *sb2;
public:
    TeeBuf(std::streambuf *buf1, std::streambuf *buf2) : sb1(buf1), sb2(buf2) { }

protected:
    int overflow(int c) override {
        if (c == EOF) return !EOF;
        else {
            int const r1 = sb1->sputc(c);
            int const r2 = sb2->sputc(c);
            return (r1 == EOF || r2 == EOF) ? EOF : c;
        }
    }
    int sync() override {
        int const r1 = sb1->pubsync();
        int const r2 = sb2->pubsync();
        return (r1 == 0 && r2 == 0) ? 0 : -1;
    }
};
